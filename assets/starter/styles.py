"""Distinct starter directions; these are example choices, not genre definitions."""
PRESETS = {
    "melodic-house": {"bpm": 120, "key": "G major", "progression": ["I", "V", "vi", "IV"],
                      "name": "原創 Melodic House", "timbres": ["soft keys", "saw pluck", "offbeat sub bass", "clap"]},
    "breakbeat": {"bpm": 132, "key": "D minor", "progression": ["i", "iv", "VI", "VII"],
                  "name": "原創 Breakbeat", "timbres": ["tine keys", "rounded organ", "syncopated bass", "short snare"]},
    "drum-and-bass": {"bpm": 172, "key": "F minor", "progression": ["i", "III", "VI", "iv"],
                      "name": "原創 Drum and Bass", "timbres": ["air pad", "long organ answer", "moving reese bass", "tight snare / ghost notes"]},
}


def apply_preset(cfg, style):
    preset = PRESETS[style]
    cfg["name"], cfg["slug"] = preset["name"], style
    cfg["music"].update(style=style, bpm=preset["bpm"], key=preset["key"], progression=list(preset["progression"]))
    if style == "melodic-house":
        return
    sections = ([(0, .12, "intro"), (.12, .4, "groove"), (.4, .5, "break"), (.5, .9, "drop"), (.9, 1, "outro")]
                if style == "breakbeat" else
                [(0, .1, "intro"), (.1, .2, "build"), (.2, .58, "drop"), (.58, .68, "break"), (.68, .9, "drop"), (.9, 1, "outro")])
    cfg["sections"] = [{"start": a * cfg["duration"], "end": b * cfg["duration"], "role": role, "label": role}
                       for a, b, role in sections]
