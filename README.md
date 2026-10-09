# EDM Music Production

An independent Codex skill for composing, arranging, synthesizing, mixing,
mastering, and revising original instrumental EDM.

獨立的 EDM 音樂製作 Skill，包含旋律與和聲、音色、編曲、混音、母帶與音訊檢查。
The instructions and production references are written in Traditional Chinese.

The included audio starter produces music on its own. No video, logo,
fonts, renderer, or other skill is required. Change its composition and instruments
to fit each brief; the starter melody is a starting point.

**[Explore this Skill on Skill Showcase →](https://bigtongue5566.github.io/?skill=edm-music-production)** ·
[Play the standalone music Demo](https://bigtongue5566.github.io/?demo=form-and-frequency-music)

## Original demo

[![Form & Frequency — animated preview](docs/media/form-and-frequency-preview.gif)](https://bigtongue5566.github.io/?demo=form-and-frequency)

**[Watch Form & Frequency with sound →](https://bigtongue5566.github.io/?demo=form-and-frequency)**

An original 90-second motion-and-music study: 1080p, 148 BPM, F minor,
procedural geometry, and a new custom Future Bass arrangement.

[Download the video](https://bigtongue5566.github.io/edm-music-production/media/form-and-frequency-90s.mp4) ·
[Hear the music](https://bigtongue5566.github.io/edm-music-production/media/form-and-frequency.m4a) ·
[Reproduce the project](examples/form-and-frequency/) ·
[Sources and licenses](examples/form-and-frequency/RIGHTS.md)

The animated preview above is an excerpt. The watch page plays the full film
with its soundtrack. The abstract visuals and music were created for this demo;
the typography uses documented OFL fonts. The source package and actual encoded
media checks are included in the example.


## More original Demos

| Work | Music | Film | Standalone soundtrack | Reproducible source |
| --- | --- | --- | --- | --- |
| Digital Pulse / 數位脈動 | 60 sec · 172 BPM · Drum & Bass | [Watch](https://bigtongue5566.github.io/?demo=digital-pulse) | [Listen](https://bigtongue5566.github.io/?demo=digital-pulse-music) | [Project](https://github.com/bigtongue5566/edm-music-production/tree/main/examples/digital-pulse) |
| Neon Drift / 霓虹漫遊 | 60 sec · 132 BPM · UK Garage | [Watch](https://bigtongue5566.github.io/?demo=neon-drift) | [Listen](https://bigtongue5566.github.io/?demo=neon-drift-music) | [Project](https://github.com/bigtongue5566/edm-music-production/tree/main/examples/neon-drift) |

Each work has a new musical arrangement and original procedural visuals,
documented sources, MIDI, editable code, and checks of the finished media.

## Silicon Explained — new original soundtrack

[Listen to 矽晶脈動](https://bigtongue5566.github.io/?demo=tsmc-explained-music) ·
[Watch the paired film](https://bigtongue5566.github.io/?demo=tsmc-explained) ·
[MIDI, synthesis source and checks](https://github.com/bigtongue5566/motion-graphics-video/tree/main/examples/tsmc-explained)

A new 90-second, 124 BPM D minor Dub Techno score for an independent, unofficial
TSMC explainer. Oscillators and generated noise supply the instruments; no third-party
recordings are sampled. The source includes the newly composed note patterns,
editable MIDI, mastering code and direct AAC/WAV verification. This is an original
creative Demo, not a TSMC commission or endorsement.

## Refreshed multi-style showcase

The four current films and soundtracks were recomposed and re-rendered on 2026-10-10:
Future Bass (148 BPM), Drum & Bass (172 BPM), UK Garage (132 BPM), and Dub Techno (124 BPM).
Their source packages retain explicit extended chords, notes, actual synthesis/automation,
MIDI and finished-media QC. These custom example implementations are separate from the
audio starter's three selectable presets. The films follow the new audio and actual kick events.

## Capabilities

The Skill includes [nine source-backed production directions](references/genre-production.md):
Melodic House, Deep House, Tech House, Dub Techno, Trance, UK Garage,
Drum & Bass, Dubstep and Future Bass. The guide draws on Ableton and
Native Instruments tutorials and interviews with El Choop, Karizma and Modestep,
with direct sources and the research date. It explains groove, bass roles,
sound modulation, layering and arrangement, rather than treating genre as a tempo label.

These are production guides for adapting a DAW or the engine. The executable
starter has the three arrangements below; the other directions require their
own implementation. See [reference analysis and musical identity](references/style-and-identity.md)
for turning a reference into an original arrangement and comparing actual results.

The local starter offers three distinct, synthesized starting arrangements:
`melodic-house`, `breakbeat`, and `drum-and-bass`. They change percussion,
instrument envelopes, bass phrasing, musical phrases, section defaults and mixing,
rather than only a display label or tempo. Use `--style` when initializing:

```powershell
python -X utf8 scripts/init_project.py --project ../broken-beat-study --duration 90 --style breakbeat
python -X utf8 scripts/init_project.py --project ../fast-bass-study --duration 90 --style drum-and-bass
```

Optional `--bpm` and `--key` override preset starting values. Omitting `--style`
preserves the original Melodic House path for older commands. Select and adapt
the actual sound direction for a new brief; a preset is a reproducible sketch,
not a completed creative decision or a professional sound library. See
[style and musical identity](references/style-and-identity.md).

- Configurable length, BPM, major/minor key, chord progression, and musical sections.
- Synthesized keys, pads, chord stabs, plucked leads, arpeggios, bass, drums, and transitions.
- Optional sampled piano with a local SoundFont and compatible FluidSynth.
- Kick-triggered ducking, frequency allocation, controlled note releases, and section contrast.
- A 48kHz/24-bit stereo WAV master, AAC soundtrack, editable MIDI, and optional aligned stems.
- Direct checks of both rendered formats: sample count, decoding, loudness, true peak,
  mono compatibility, unintended silence, and the final fade.
- Music and instrument provenance, including an optional SoundFont fingerprint.

## Install as a Codex skill

Clone into the standard Codex skills directory on Windows:

```powershell
git clone https://github.com/bigtongue5566/edm-music-production.git "$env:USERPROFILE\.codex\skills\edm-music-production"
```

If you configured a different `CODEX_HOME`, use its `skills/edm-music-production`
directory. Preserve an existing installation by choosing an empty destination.

Example invocation:

```text
用 $edm-music-production 製作一首 90 秒的旋律型 EDM，
有柔和鋼琴開場、兩段有力的高潮與自然收尾，交付音檔、MIDI 和分軌。
```

## Run the audio starter

Use Python 3.12 and `uv`. From the repository root:

```powershell
python -X utf8 scripts/init_project.py --project ../my-edm --duration 90 --bpm 120 --key "G major" --stems
uv venv ../my-edm/work/.venv --python 3.12
uv pip install --python ../my-edm/work/.venv/Scripts/python.exe -r ../my-edm/work/requirements.txt
```

Edit `../my-edm/project.json` for the title, length, tempo, key, chord degrees,
section timings, mastering targets, and instruments. Then:

```powershell
../my-edm/work/.venv/Scripts/python.exe -X utf8 ../my-edm/work/compose_edm.py --project ../my-edm
../my-edm/work/.venv/Scripts/python.exe -X utf8 ../my-edm/work/finish_music.py --project ../my-edm
```

On other platforms, use the corresponding `venv/bin/python` path. The audio
pipeline needs NumPy, SciPy, Mido, and imageio-ffmpeg. FFmpeg is provided by
imageio-ffmpeg; no system installation is required.

The initializer also accepts `--name` and `--slug`, validates settings before
writing, and refuses to overwrite existing files. Passing `--duration` scales
the default sections; edit their timing afterward for the desired musical form.

## Deliverables

| Output | Purpose |
| --- | --- |
| `<slug>-master.wav` | 48kHz/24-bit stereo master with the exact requested sample count |
| `<slug>.m4a` | AAC at 256kbps for convenient playback |
| `<slug>-music.mid` | Editable note and instrument tracks |
| `stems/<slug>-*.wav` | Optional aligned Float32 premaster stems |
| `<slug>-qc.json` | Measurements from the actual WAV and AAC |
| `<slug>-provenance.json` | Composition, instruments, sections, and source details |
| `<slug>-production.md` | Human-readable production notes |

The stems share gain and fades; summing them reconstructs `work/score-mix.wav`.
They are not separately normalized to loudness targets. The master undergoes
another loudness-processing stage. MIDI uses GM instrument suggestions and will
not reproduce the included synthesizers exactly.

## Keys and arrangement

The default progression is I–V–vi–IV in G major. Selecting a minor key in the
initializer uses i–VI–III–VII. Supported degrees and section behavior are in
[the project schema](references/music-project.md).

Sections use `intro`, `groove`, `build`, `drop`, `break`, and `outro`. The main
harmony follows bars; section accents and drum changes follow the requested
times. Align boundaries to bars when all instruments should change together,
or adapt the local phrase. An arbitrary duration is preserved with a tonic
resolution and fade. Loopable music requires a separate loop ending.

For sampled piano, configure local `music.soundfont` and `music.fluidsynth`
paths and record the sound library's source and license. No sampled bank or
external executable is bundled. Without a SoundFont, the keyboard is synthesized
and identified as such in the provenance.

## Production references

- [Skill instructions](SKILL.md)
- [Composition, sound design, and mixing](references/composition-and-mix.md)
- [Music project settings](references/music-project.md)
- [Local workflow and provenance](references/local-workflow.md)

This skill focuses on music. For branded video production, see the separate
[motion-graphics-video](https://github.com/bigtongue5566/motion-graphics-video) skill.

## Verification

Run the included end-to-end smoke tests after installing the audio dependencies:

```powershell
../my-edm/work/.venv/Scripts/python.exe -X utf8 -m unittest discover -s tests -v
```

They render a non-bar-length minor-key track, verify MIDI and audio output,
check stem recombination and deterministic rendering, and exercise the
initializer's rejection of invalid settings and existing files.

Signal checks and symbolic chord audits do not prove that music sounds good.
Listen to the arrangement, transitions, instrument balance, and ending to
assess musical quality. The default master targets are −16 LUFS and −2 dBTP;
choose suitable targets for the actual use.

## License

The skill documentation, original composition template, and synthesis code are
available under the [MIT License](LICENSE).
The synthesis primitives were originally released as part of
[motion-graphics-video](https://github.com/bigtongue5566/motion-graphics-video).
Dependencies, SoundFonts, instrument samples, and other external assets retain
their respective licenses. No sampled instrument banks or third-party songs are bundled.
