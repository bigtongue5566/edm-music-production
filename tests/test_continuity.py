"""Regression tests for audible release, common-tone ties and hidden short gaps."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace
import mido
from scipy.io import wavfile
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'assets/starter'))
import instruments as ins
from compose_edm import Score
from continuity import sustained_pad, connected_bass, micro_dynamics, apply_continuity


class ContinuityRegression(unittest.TestCase):
    def setUp(self):
        self.folder=tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        root=Path(self.folder.name)
        (root/'work').mkdir();(root/'outputs').mkdir()
        cfg=json.loads((ROOT/'assets/starter/project.json').read_text(encoding='utf-8'))
        cfg['duration']=6
        cfg['music'].update(bpm=120,key='G major',progression=['I','IV'])
        cfg['sections']=[{'start':0,'end':6,'role':'drop','label':'test'}]
        self.score=Score(root,cfg)

    def test_default_repair_preserves_existing_density(self):
        s = self.score
        s.note('pad', .5, .1, 67, .12, sound=ins.pad_voice(67, .1))
        before = {name: audio.copy() for name, audio in s.stems.items()}
        events = [dict(event) for event in s.events]
        apply_continuity(s)
        self.assertEqual(s.events, events)
        for name in before:
            np.testing.assert_array_equal(s.stems[name], before[name])
        s.cfg['music']['continuity'] = {'tie_pad': True, 'room_wet': .08}
        apply_continuity(s)
        self.assertGreater(np.max(np.abs(s.stems['pad'][:int(.2*s.sr)])), .01)
        self.assertGreater(np.max(np.abs(s.stems['effects'])), .001)

    def test_midi_does_not_send_all_sound_off_at_harmony_boundaries(self):
        s=self.score
        s.sf=s.root/'unused-soundfont.sf2'
        s.note('keys',1.9,.05,67,.1,boundary=2)
        path=s.root/'work/keys.mid'
        s.write_midi(path,keys_only=True)
        midi=mido.MidiFile(path,charset='utf-8')
        controls=[message.control for track in midi.tracks for message in track
                  if message.type=='control_change']
        self.assertNotIn(120,controls,'All Sound Off must not kill compatible releases')
        offs=[message for track in midi.tracks for message in track if message.type=='note_off']
        self.assertEqual(len(offs),1,'The real MIDI note-off must still be exported')

    def test_sampled_bus_preserves_a_release_crossing_shared_harmony(self):
        s=self.score
        s.sf=s.root/'test.sf2'
        s.sf.write_bytes(b'RIFF'+(4).to_bytes(4,'little')+b'sfbk')
        s.cfg['music']['fluidsynth']='fake-engine'
        s.note('keys',1.9,.05,67,.1,boundary=2)
        t=np.arange(s.n)/s.sr
        tone=np.sin(2*np.pi*392*t).astype(np.float32)*.1
        release=tone*((t>=1.9)&(t<2.15))
        wavfile.write(s.root/'work/keys-render.wav',s.sr,np.column_stack([release,release]))
        with patch('compose_edm.subprocess.run',return_value=SimpleNamespace(
                returncode=0,stdout=b'',stderr=b'')):
            s.render_sampled_keys()
        body=s.stems['keys'][int(1.96*s.sr):int(1.98*s.sr)]
        seam=s.stems['keys'][int(1.999*s.sr):int(2.001*s.sr)]
        self.assertGreater(np.sqrt(np.mean(seam**2)),np.sqrt(np.mean(body**2))*.7)

    def test_note_off_does_not_cut_audible_release(self):
        s=self.score
        s.note('keys',.5,.1,67,1,sound=ins.organ_voice(67,.1),boundary=2)
        after=s.stems['keys'][round(.62*s.sr):round(.72*s.sr)]
        self.assertGreater(float(np.sqrt(np.mean(after**2))),.02)
        self.assertAlmostEqual(s.events[0]['duration'],.1)
        self.assertGreater(s.events[0]['sounding_duration'],.25)

    def test_release_crosses_only_compatible_harmony(self):
        s=self.score
        s.note('keys',1.95,.05,67,1,sound=ins.organ_voice(67,.05),boundary=2)
        self.assertGreater(np.max(np.abs(s.stems['keys'][2*s.sr:round(2.12*s.sr)])),.01)
        s.stems['keys'].fill(0)
        s.note('keys',1.95,.05,71,1,sound=ins.organ_voice(71,.05),boundary=2)
        self.assertEqual(float(np.max(np.abs(s.stems['keys'][2*s.sr:]))),0)
        self.assertLess(float(np.max(np.abs(s.stems['keys'][2*s.sr-1]))),1e-5)

    def test_shared_pad_note_is_tied_across_the_bar(self):
        s=self.score
        sustained_pad(s,.12)
        tied=[e for e in s.events if e['stem']=='pad' and e['time']==0 and e['duration']==6]
        self.assertTrue(tied,'A shared G must continue through I to IV')
        before=s.stems['pad'][round(1.75*s.sr):round(1.95*s.sr)]
        seam=s.stems['pad'][round(1.98*s.sr):round(2.02*s.sr)]
        self.assertGreater(np.sqrt(np.mean(seam**2)),np.sqrt(np.mean(before**2))*.5)

    def test_legato_bass_keeps_energy_and_phase_at_note_change(self):
        s=self.score
        s.events=[{'stem':'bass','time':.25,'duration':.1,'note':43,'velocity':80},
                  {'stem':'bass','time':1,'duration':.1,'note':43,'velocity':80}]
        connected_bass(s,'future-bass')
        edge=s.stems['bass'][round(.98*s.sr):round(1.02*s.sr)]
        body=s.stems['bass'][round(.70*s.sr):round(.90*s.sr)]
        self.assertGreater(np.sqrt(np.mean(edge**2)),np.sqrt(np.mean(body**2))*.7)
        self.assertLess(float(np.max(np.abs(np.diff(edge,axis=0)))),.01)

    def test_micro_windows_find_gaps_hidden_by_one_second_rms(self):
        sr=48000;t=np.arange(sr*2)/sr
        sound=np.sin(2*np.pi*440*t)*(t%.25<.04)
        self.assertGreater(np.sqrt(np.mean(sound[:sr]**2)),.1)
        report=micro_dynamics(sound[:,None],sr,[{'start':0,'end':2,'role':'drop'}])
        self.assertGreaterEqual(report['regions'][0]['longest_deep_trough_ms'],190)


if __name__=='__main__': unittest.main()
