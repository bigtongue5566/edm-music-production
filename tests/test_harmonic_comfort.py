"""Cross-part dissonance is different from all notes being in one key."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'assets/starter'))
from harmonic_comfort import overlapping_dissonances, check_profile


def event(note,stem='keys',start=0,duration=1,**extra):
    return dict(note=note,stem=stem,time=start,duration=duration,**extra)


class HarmonicComfort(unittest.TestCase):
    def test_major_minor_triads_and_inversions_are_allowed(self):
        for notes in ([60,64,67],[50,53,57],[55,59,64],[48,55,64,72]):
            self.assertFalse(overlapping_dissonances([event(n) for n in notes]))

    def test_default_rejects_cross_stem_diatonic_ninth(self):
        notes=[event(60,'pad'),event(74,'lead')]
        with self.assertRaisesRegex(ValueError,'Consonant profile'):
            check_profile(notes,{})
        report=check_profile(notes,{'harmonic_profile':'intentional-tension','tension_intent':'requested ninth'})
        self.assertEqual(report['tracked_overlap_conflicts'][0]['semitones'],14)

    def test_release_overlap_is_checked_but_nonoverlapping_notes_are_allowed(self):
        dry=[event(60,duration=.1),event(62,'lead',start=.2)]
        self.assertFalse(overlapping_dissonances(dry))
        dry[0]['sounding_duration']=.4
        self.assertTrue(overlapping_dissonances(dry))

    def test_drum_notes_do_not_create_false_tritones(self):
        self.assertFalse(overlapping_dissonances([event(60),event(42,'drums')]))


if __name__=='__main__': unittest.main()
