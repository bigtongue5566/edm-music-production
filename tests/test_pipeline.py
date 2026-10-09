"""Meaningful acceptance tests of the independent audio production path."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import wave

import mido
import numpy as np
from scipy.io import wavfile

ROOT = Path(__file__).resolve().parents[1]


def run(*args, expect_success=True):
    p = subprocess.run([sys.executable, "-X", "utf8", *map(str, args)], capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    if expect_success and p.returncode:
        raise AssertionError(p.stdout + p.stderr)
    return p


class AudioPipeline(unittest.TestCase):
    def test_minor_non_bar_length_stems_midi_and_master(self):
        with tempfile.TemporaryDirectory(prefix="edm-pipeline-") as folder:
            project = Path(folder) / "song"
            run(ROOT / "scripts" / "init_project.py", "--project", project, "--duration", "7.3",
                "--bpm", "124", "--key", "F# minor", "--stems", "--name", "小調測試")
            run(project / "work" / "compose_edm.py", "--project", project)
            run(project / "work" / "finish_music.py", "--project", project)
            qc = json.loads((project / "outputs" / "melodic-house-qc.json").read_text(encoding="utf-8"))
            self.assertEqual(qc["wav"]["samples"], 350400)
            self.assertEqual(qc["key"], "F# minor")
            self.assertEqual(qc["full_decode_errors"], 0)
            self.assertEqual(qc["unexpected_chord_conflicts"], 0)
            with wave.open(str(project / "outputs" / "melodic-house-master.wav")) as source:
                self.assertEqual((source.getnchannels(), source.getsampwidth(), source.getframerate()), (2, 3, 48000))
            rate, mix = wavfile.read(project / "work" / "score-mix.wav")
            paths = sorted((project / "outputs" / "stems").glob("*.wav"))
            self.assertEqual(len(paths), 8)
            tracks = []
            for path in paths:
                stem_rate, stem = wavfile.read(path)
                self.assertEqual(stem_rate, rate)
                self.assertEqual(stem.shape, mix.shape)
                tracks.append(stem)
            np.testing.assert_allclose(sum(tracks), mix, atol=2e-7, rtol=2e-6)
            midi = mido.MidiFile(project / "outputs" / "melodic-house-music.mid", charset="utf-8")
            signature = [message.key for track in midi.tracks for message in track if message.type == "key_signature"]
            self.assertEqual(signature, ["F#m"])
            self.assertAlmostEqual(midi.length, 7.3, delta=.002)
            original_hash = hashlib.sha256((project / "work" / "score-mix.wav").read_bytes()).digest()
            run(project / "work" / "compose_edm.py", "--project", project)
            self.assertEqual(hashlib.sha256((project / "work" / "score-mix.wav").read_bytes()).digest(), original_hash)
            settings = (project / "project.json").read_bytes()
            rejected = run(ROOT / "scripts" / "init_project.py", "--project", project, expect_success=False)
            self.assertNotEqual(rejected.returncode, 0)
            self.assertEqual((project / "project.json").read_bytes(), settings)

    def test_invalid_settings_leave_no_project(self):
        with tempfile.TemporaryDirectory(prefix="edm-invalid-") as folder:
            for i, arguments in enumerate([( "--duration", "-4"), ("--duration", "nan"),
                                            ("--bpm", "0"), ("--key", "H major"), ("--slug", "../unsafe"), ("--style", "unknown")]):
                target = Path(folder) / f"invalid-{i}"
                p = run(ROOT / "scripts" / "init_project.py", "--project", target, *arguments, expect_success=False)
                self.assertNotEqual(p.returncode, 0)
                self.assertFalse(target.exists())

    def test_styles_change_real_rhythm_and_audio_at_identical_tempo_and_key(self):
        mixes = []
        kicks = []
        with tempfile.TemporaryDirectory(prefix="edm-style-") as folder:
            for style in ["melodic-house", "breakbeat", "drum-and-bass"]:
                project = Path(folder) / style
                run(ROOT / "scripts/init_project.py", "--project", project, "--duration", "8.3",
                    "--style", style, "--bpm", "128", "--key", "A minor")
                path = project / "project.json"
                cfg = json.loads(path.read_text(encoding="utf-8"))
                cfg["sections"] = [{"start":0,"end":8.3,"role":"drop","label":"same excerpt"}]
                cfg["music"]["progression"] = ["i", "VI", "III", "VII"]
                path.write_text(json.dumps(cfg), encoding="utf-8")
                run(project / "work/compose_edm.py", "--project", project)
                run(project / "work/finish_music.py", "--project", project)
                qc = json.loads((project / "outputs" / (style + "-qc.json")).read_text(encoding="utf-8"))
                self.assertEqual(qc["full_decode_errors"], 0)
                self.assertEqual(qc["unexpected_chord_conflicts"], 0)
                self.assertEqual(qc["wav"]["samples"], 398400)
                events = json.loads((project / "work/note-events.json").read_text(encoding="utf-8"))
                first_bar = [e["time"] * 128 / 60 for e in events if e["stem"] == "drums" and e["note"] == 36 and e["time"] < 240 / 128]
                kicks.append(first_bar)
                mixes.append(hashlib.sha256((project / "work/score-mix.wav").read_bytes()).digest())
        self.assertEqual(len(set(mixes)), 3)
        self.assertTrue(all(abs(t-round(t)) < 1e-6 for t in kicks[0]))
        self.assertTrue(all(any(abs(t-round(t)) > .1 for t in pattern) for pattern in kicks[1:]))
        self.assertNotEqual(kicks[1], kicks[2])


if __name__ == "__main__":
    unittest.main()
