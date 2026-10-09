"""Create an audio-only EDM project; validate first and never overwrite files."""
import argparse
import importlib.util
import json
from pathlib import Path
import shutil


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", type=Path, required=True)
    ap.add_argument("--duration", type=float)
    ap.add_argument("--bpm", type=float)
    ap.add_argument("--key", help="For example G major or A minor")
    ap.add_argument("--name")
    ap.add_argument("--slug")
    ap.add_argument("--stems", action="store_true")
    ap.add_argument("--style", choices=["melodic-house", "breakbeat", "drum-and-bass"], default="melodic-house")
    args = ap.parse_args()
    source = Path(__file__).resolve().parents[1] / "assets" / "starter"
    target = args.project.resolve()
    spec = importlib.util.spec_from_file_location("edm_config", source / "projectlib.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cfg = json.loads((source / "project.json").read_text(encoding="utf-8"))
    style_spec = importlib.util.spec_from_file_location("edm_styles", source / "styles.py")
    style_module = importlib.util.module_from_spec(style_spec)
    style_spec.loader.exec_module(style_module)
    style_module.apply_preset(cfg, args.style)
    if args.duration is not None:
        scale = args.duration / cfg["duration"]
        for section in cfg["sections"]:
            section["start"] *= scale
            section["end"] *= scale
        cfg["duration"] = args.duration
        cfg["sections"][-1]["end"] = args.duration
    if args.bpm is not None:
        cfg["music"]["bpm"] = args.bpm
    if args.key:
        cfg["music"]["key"], _ = module.normalize_key(args.key)
        if cfg["music"]["key"].endswith("minor") and any(d.isupper() and d in ["I", "IV"] for d in cfg["music"]["progression"]):
            cfg["music"]["progression"] = ["i", "VI", "III", "VII"]
        elif cfg["music"]["key"].endswith("major") and "i" in cfg["music"]["progression"]:
            cfg["music"]["progression"] = ["I", "IV", "vi", "V"]
    if args.name:
        cfg["name"] = args.name
    if args.slug:
        cfg["slug"] = args.slug
    cfg["music"]["export_stems"] = args.stems
    try:
        module.validate(cfg)
    except (ValueError, TypeError, KeyError) as error:
        ap.error(str(error))
    files = [p for p in source.iterdir() if p.is_file() and p.name != "project.json"]
    conflicts = [str(p) for p in [target / "project.json", *[target / "work" / p.name for p in files]] if p.exists()]
    if conflicts:
        ap.error("Existing files would be overwritten: " + ", ".join(conflicts))
    (target / "work" / "assets").mkdir(parents=True, exist_ok=True)
    (target / "outputs").mkdir(exist_ok=True)
    for file in files:
        shutil.copy2(file, target / "work" / file.name)
    (target / "project.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"MUSIC_PROJECT_CREATED {target}")


if __name__ == "__main__":
    main()
