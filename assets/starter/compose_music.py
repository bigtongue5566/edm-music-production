"""Canonical electronic-music entry point; legacy compose_edm.py remains usable."""
import argparse
from pathlib import Path

from compose_edm import Score
from continuity import apply_continuity
from projectlib import load

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project',type=Path,required=True)
    args=parser.parse_args()
    root,cfg=load(args.project)
    score=Score(root,cfg)
    score.arrange()
    apply_continuity(score)
    score.audit()
    score.mix()
    score.write_midi(root/'outputs'/f"{cfg['slug']}-music.mid")
    print('MUSIC_COMPLETE',flush=True)
