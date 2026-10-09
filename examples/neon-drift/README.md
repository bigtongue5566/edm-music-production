# 霓虹漫遊 — Neon Drift

A new 60-second original motion/music Demo, in A major at 96 BPM.
Music style: **Synthwave / Electronic**. New hooks, drum and bass patterns,
electronic synthesis, procedural scenes, and animation were created for this work.

[Watch the film](https://bigtongue5566.github.io/?demo=neon-drift) ·
[Play the music](https://bigtongue5566.github.io/?demo=neon-drift-music) ·
[Download sources](https://bigtongue5566.github.io/edm-music-production/media/neon-drift-source.zip)

## Reproduce on Windows

From this example directory, with Python 3.12 and uv:

```powershell
uv venv work/.venv --python 3.12
uv pip install --python work/.venv/Scripts/python.exe -r requirements.txt
work/.venv/Scripts/python.exe -X utf8 download_fonts.py
Copy-Item production/*.py work/
work/.venv/Scripts/python.exe -X utf8 work/compose_gallery.py --project .
work/.venv/Scripts/python.exe -X utf8 work/finish_music.py --project .
work/.venv/Scripts/python.exe -X utf8 work/render_gallery.py preview --project .
work/.venv/Scripts/python.exe -X utf8 work/render_gallery.py render --project .
work/.venv/Scripts/python.exe -X utf8 work/finish_gallery.py --project .
```

On other platforms use the corresponding venv/bin/python and copy command.
The first font download uses pinned upstream versions and verifies SHA-256.
The reproduction scripts render locally and do not publish to any service.

Outputs include the 1080p/30fps MP4, 48kHz/24-bit stereo WAV master, AAC,
MIDI, previews, and direct audio/video QC. MIDI instrument suggestions differ
from the custom synthesis used in the finished recording.

The source extends the MIT Skill production primitives. `original_renderer.py`
supplies shared font, audio-analysis, frame-transition, and encoding utilities;
the new circuit/neon scenes are implemented in `render_gallery.py`.

Objective note, decoding, loudness, mono, tail and motion checks passed. These
checks do not certify subjective listening quality. See [rights](RIGHTS.md),
[sources](sources.json), [audio QC](audio-qc.json), and [video QC](video-qc.json).
