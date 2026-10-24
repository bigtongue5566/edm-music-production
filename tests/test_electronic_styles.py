"""Exercise actual rendered differences, free timing and the new CLI entrypoint."""
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np
from scipy.io import wavfile

from test_pipeline import ROOT, run


class ElectronicStyles(unittest.TestCase):
    def test_six_new_styles_render_and_master_with_distinct_rhythm(self):
        patterns={}
        with tempfile.TemporaryDirectory(prefix='electronic-families-') as folder:
            for style in ['techno','trance','dubstep','trap','ambient','downtempo']:
                with self.subTest(style=style):
                    project=Path(folder)/style
                    run(ROOT/'scripts/init_project.py','--project',project,'--duration','8.3',
                        '--style',style,'--bpm','120','--key','A minor','--stems')
                    path=project/'project.json';cfg=json.loads(path.read_text(encoding='utf-8'))
                    cfg['sections']=[{'start':0,'end':8.3,'role':'drop','label':'same excerpt'}]
                    cfg['music']['progression']=['i']
                    path.write_text(json.dumps(cfg),encoding='utf-8')
                    run(project/'work/compose_music.py','--project',project)
                    run(project/'work/finish_music.py','--project',project)
                    qc=json.loads((project/f'outputs/{style}-qc.json').read_text(encoding='utf-8'))
                    self.assertEqual(qc['wav']['samples'],398400)
                    self.assertEqual(qc['full_decode_errors'],0)
                    events=json.loads((project/'work/note-events.json').read_text(encoding='utf-8'))
                    drums=[(e['note'],round(e['time']*2,5)) for e in events
                           if e['stem']=='drums' and e['time']<2]
                    patterns[style]=drums
                    sr,bass=wavfile.read(project/f'outputs/stems/{style}-bass.wav')
                    self.assertGreater(float(np.mean(bass**2)),1e-8)
                    if style=='ambient':
                        self.assertFalse(drums)
                        _,sound=wavfile.read(project/f'outputs/stems/{style}-drums.wav')
                        self.assertEqual(float(np.abs(sound).max()),0)
                    else:self.assertTrue(drums)
        for style in ['techno','trance']:
            self.assertEqual([t for n,t in patterns[style] if n==36],[0,1,2,3])
        for style in ['dubstep','trap']:
            self.assertEqual([t for n,t in patterns[style] if n==38],[2])
        self.assertTrue(any(abs(t*4-round(t*4))>.1 for n,t in patterns['trap'] if n==42))
        self.assertNotEqual(patterns['trap'],patterns['dubstep'])
        self.assertNotEqual(patterns['downtempo'],patterns['techno'])

    def test_ambient_changes_harmony_in_seconds_not_every_four_beats(self):
        with tempfile.TemporaryDirectory(prefix='electronic-free-') as folder:
            project=Path(folder)/'ambient'
            run(ROOT/'scripts/init_project.py','--project',project,'--duration','25.3','--style','ambient')
            run(project/'work/compose_music.py','--project',project)
            data=json.loads((project/'work/music-metadata.json').read_text(encoding='utf-8'))
            self.assertEqual(data['pulse'],'free')
            self.assertEqual([h['start'] for h in data['harmony']],[0,12,24])
            self.assertEqual(data['harmony'][-1]['name'],'vi')
            self.assertIn('reference tempo only',data['tempo_note'])

    def test_unsupported_style_fails_instead_of_falling_back_to_house(self):
        with tempfile.TemporaryDirectory(prefix='electronic-custom-') as folder:
            project=Path(folder)/'unsupported'
            result=run(ROOT/'scripts/init_project.py','--project',project,'--style','hardstyle',expect_success=False)
            self.assertNotEqual(result.returncode,0)
            self.assertFalse(project.exists())


if __name__=='__main__':unittest.main()
