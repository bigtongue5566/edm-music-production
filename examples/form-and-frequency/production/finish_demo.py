"""Mux the finished original film and verify the actual encoded video and audio."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

import imageio_ffmpeg
import numpy as np
from PIL import Image


def finish(root):
    root = Path(root).resolve()
    cfg = json.loads((root / "project.json").read_text(encoding="utf-8"))
    out, work = root / "outputs", root / "work"
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    movie = out / (cfg["slug"] + "-90s.mp4")

    def run(arguments, log=None, binary=False):
        p = subprocess.run([ff, "-hide_banner", *arguments], capture_output=True,
                           text=not binary, encoding=None if binary else "utf-8", errors=None if binary else "replace")
        if log:
            (work / log).write_text(p.stdout + "\n" + p.stderr, encoding="utf-8")
        if p.returncode:
            raise RuntimeError(str(p.stderr)[-3000:])
        return p

    run(["-y", "-i", str(work / "picture.mp4"), "-i", str(out / (cfg["slug"] + ".m4a")),
         "-map", "0:v:0", "-map", "1:a:0", "-c", "copy", "-t", str(cfg["duration"]),
         "-movflags", "+faststart", "-metadata", "title=Form & Frequency / Original motion and music study",
         "-metadata", "comment=Original procedural geometry and synthesized music; see sources and licenses.",
         str(movie)], "mux.log")
    metadata = run(["-i", str(movie), "-map", "0", "-c", "copy", "-f", "null", "-"], "encoded-metadata.log")
    match = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", metadata.stderr)
    seconds = int(match[1]) * 3600 + int(match[2]) * 60 + float(match[3])
    assert abs(seconds - cfg["duration"]) <= .02, seconds
    video = cfg["video"]
    assert re.search(r"Video: h264[^\n]*1920x1080[^\n]*30 fps", metadata.stderr), metadata.stderr[-1000:]
    assert re.search(r"Audio: aac[^\n]*48000 Hz, stereo", metadata.stderr)
    decode = run(["-v", "error", "-nostats", "-i", str(movie), "-map", "0:v:0", "-an",
                  "-progress", "pipe:1", "-f", "null", "-"], "video-full-decode.log")
    frame_count = int(re.findall(r"frame=(\d+)", decode.stdout)[-1])
    assert frame_count == round(cfg["duration"] * video["fps"]), frame_count
    assert not decode.stderr.strip(), decode.stderr
    levels = run(["-nostats", "-i", str(movie), "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"], "final-audio-meter.log")
    summary = levels.stderr[levels.stderr.rfind("Summary:"):]
    lufs = float(re.search(r"I:\s*([-\d.]+) LUFS", summary)[1])
    peak = float(re.search(r"Peak:\s*([-\d.]+) dBFS", summary)[1])
    assert abs(lufs - cfg["music"]["lufs"]) < 1.5 and peak < -.5, (lufs, peak)
    sound = run(["-v", "error", "-i", str(movie), "-map", "0:a:0", "-f", "f32le", "-ac", "2", "-ar", "48000", "pipe:1"], binary=True)
    assert not sound.stderr
    samples = np.frombuffer(sound.stdout, dtype="<f4").reshape(-1, 2)
    assert np.isfinite(samples).all() and np.abs(samples).max() < 1
    decoded_seconds = len(samples) / 48000
    assert abs(decoded_seconds - cfg["duration"]) <= 1024 / 48000 + .001
    qc = work / "qc"
    qc.mkdir(exist_ok=True)
    times = [3., 18., 26., 40., 48., 57., 70., 78., 86., 89.95, 6., 6.5, 26.5, 22.4, 22.8]
    paths = {}
    for i, t in enumerate(times):
        target = qc / f"frame-{i:02d}.jpg"
        run(["-y", "-v", "error", "-ss", str(t), "-i", str(movie), "-frames:v", "1", "-q:v", "2", str(target)])
        assert target.is_file() and target.stat().st_size > 0, t
        paths[t] = target
    board = Image.new("RGB", (1920, 1080), "#080C16")
    for i, t in enumerate(times[:9]):
        image = Image.open(paths[t]).convert("RGB")
        assert image.size == (1920, 1080)
        board.paste(image.resize((640, 360), Image.Resampling.LANCZOS), ((i % 3) * 640, (i // 3) * 360))
    board.save(out / (cfg["slug"] + "-encoded-storyboard.jpg"), quality=94)
    movement = {}
    for first, second, label in [(6., 6.5, "intro_geometry"), (26., 26.5, "drop_geometry")]:
        a = np.asarray(Image.open(paths[first]).crop((960, 150, 1800, 900)).resize((420, 375)), dtype=float)
        b = np.asarray(Image.open(paths[second]).crop((960, 150, 1800, 900)).resize((420, 375)), dtype=float)
        difference = float(np.abs(a - b).mean())
        assert difference > .3, (label, difference)
        movement[label] = round(difference, 3)
    report = {"status": "FINAL_MP4_VERIFIED", "file": movie.name, "duration_seconds": seconds,
              "width": 1920, "height": 1080, "fps": 30, "fully_decoded_video_frames": frame_count,
              "audio_sample_rate": 48000, "audio_channels": 2, "audio_decoded_seconds": round(decoded_seconds, 5),
              "integrated_lufs": lufs, "true_peak_dbtp": peak, "full_decode_errors": 0,
              "sampled_encoded_frames": len(times), "geometry_motion_difference": movement,
              "music_bpm": cfg["music"]["bpm"], "music_key": cfg["music"]["key"],
              "mp4_bytes": movie.stat().st_size, "mp4_sha256": hashlib.sha256(movie.read_bytes()).hexdigest(),
              "limits": "Encoded-media and frame checks are objective verification; subjective listening quality is not certified."}
    (out / (cfg["slug"] + "-video-qc.json")).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    finish(parser.parse_args().project)
