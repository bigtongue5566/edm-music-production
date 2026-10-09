# Form & Frequency / 聲形之間

A 90-second original motion-and-music study, composed and animated for the
`edm-music-production` showcase. The typography is in Traditional Chinese and English.

[Watch with sound](https://bigtongue5566.github.io/edm-music-production/)

## The film

- 1920 × 1080, 30fps, exactly 90 seconds / 2700 video frames.
- Original Melodic House score: 128 BPM, D major, 48 bars in 4/4.
- New chord-aware six-note phrases over vi–IV–I–V, with a tonic ending.
- Entirely synthesized keys, pad, chord stabs, lead, arpeggio, bass, drums, and effects.
- Procedural torus curves, translucent 3D modules, flowing connections, waves, and orbits.
- The spectrum geometry uses measurements of the actual audio master; animation accents
  and scene boundaries follow the shared musical timeline.
- Openly licensed Noto Sans CJK TC and Space Grotesk typography.

The project is an abstract artwork rather than a company advertisement. Its geometry,
new melodic phrase, arrangement, and rendered audio were made for this demo. The
audio production code builds on this repository's MIT-licensed starter.

## Reproduce the complete film

Use Python 3.12. From this example directory:

```powershell
uv venv .venv --python 3.12
uv pip install --python .venv/Scripts/python.exe -r requirements.txt
.venv/Scripts/python.exe -X utf8 download_fonts.py
.venv/Scripts/python.exe -X utf8 production/compose_edm.py --project .
.venv/Scripts/python.exe -X utf8 production/finish_music.py --project .
.venv/Scripts/python.exe -X utf8 production/render_demo.py preview --project .
.venv/Scripts/python.exe -X utf8 production/render_demo.py render --project .
.venv/Scripts/python.exe -X utf8 production/finish_demo.py --project .
```

On other platforms, use `.venv/bin/python`. FFmpeg comes from imageio-ffmpeg.
The font downloader fetches only the four explicitly recorded files at pinned
official revisions and verifies their SHA-256 fingerprints. It preserves existing
files that have different content. The full CJK font is downloaded when reproducing
the project; it is not bundled in this source package.

Generated intermediates live in `work/`, and finished video, audio, MIDI, posters,
and quality reports live in `outputs/`. The renderer reads the completed WAV master,
so run audio production before rendering.

## Verification

`audio-qc.json` and `video-qc.json` record measurements of the published result.
The final MP4 was fully decoded, checked for the exact number of frames and audio
streams, and sampled for visible motion and typography. Audio checks include
loudness, true peak, finite samples, harmonic conflicts, ending fade, and mono
compatibility. These checks do not certify subjective musical quality.

`sources.json` records the creative scope and each external font's immutable source,
license, byte count, SHA-256, and Git blob fingerprint. See [RIGHTS.md](RIGHTS.md)
and `licenses/` for usage and attribution.

## License

The example's code and original demonstration media are provided under the
[MIT License](LICENSE), with a copy included in the source archive.
The external fonts remain under SIL Open Font License 1.1. Their licenses do not
turn the rendered film into an OFL-licensed font. Retain the applicable license
and copyright notices when redistributing source or font software.
