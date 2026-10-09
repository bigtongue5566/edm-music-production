"""Two custom arrangements with new hooks, voicings, timbres, and drum patterns."""
import argparse
from functools import lru_cache
import math
from pathlib import Path
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--project", type=Path, required=True)
args = parser.parse_args()
sys.path.insert(0,str(args.project.resolve() / "work"))
import numpy as np
import instruments as ins
from compose_edm import Score
from projectlib import load


@lru_cache(maxsize=128)
def neon_voice(note, length, lead=False):
    t = np.arange(round(length*ins.SR))/ins.SR
    f = ins.hz(note)
    sound = np.zeros((len(t),2))
    for channel,cents in [(0,-3),(1,3)]:
        freq=f*2**(cents/1200)
        for harmonic in range(1,min(35,int(16000//freq))+1):
            weight=1/harmonic**1.55/math.sqrt(1+(harmonic*freq/(1800 if lead else 1200))**6)
            sound[:,channel]+=weight*np.sin(2*math.pi*freq*harmonic*t+.22*harmonic)
        sound[:,channel]=ins.soften(sound[:,channel],.022 if lead else .075,min(.15,length/4))
    sound *= (.65+.35*np.exp(-t*2))[:,None]
    return (sound*.30).astype(np.float32)


class GalleryScore(Score):
    def arrange(self):
        neon=self.cfg["music"]["arrangement"]=="neon"
        kick,clap,hat=ins.kick(),ins.clap(),ins.hat()
        for index,chord in enumerate(self.harmony):
            a,b,role=chord["start"],chord["end"],chord["role"]
            span=b-a
            drop=role=="drop"
            active=role in ("groove","build","drop")
            for pitch in chord["voices"]:
                length=span-.04
                self.note("pad",a,length,pitch+12,.12 if neon else .085,
                          sound=neon_voice(pitch+12,length) if neon else ins.pad_voice(pitch+12,length),boundary=b)
            if not active:
                for j,off in enumerate([0,1.5,3]):
                    start=a+off*self.beat
                    length=min(self.beat*.85,b-start-.03)
                    if length>.01:
                        pitch=chord["voices"][[2,1,0][j]]+12
                        self.note("keys",start,length,pitch,.20 if neon else .16,
                                  sound=self.keys(pitch,length),boundary=b)
            if active:
                # Different phrase shapes: sustained retro hook vs syncopated pulse hook.
                offsets=[0,.5,1.5,2.5] if neon else [0,.5,1.25,2,2.75,3.5]
                degrees=([0,2,1,2] if index%2==0 else [2,1,0,1]) if neon else ([1,0,2,1,2,0] if index%2==0 else [2,1,0,2,0,1])
                for j,(off,degree) in enumerate(zip(offsets,degrees)):
                    pitch=chord["voices"][degree]+(12 if neon else 24)
                    length=self.beat*([.42,.75,.72,.92][j] if neon else [.30,.38,.45,.38,.35,.42][j])
                    sound=neon_voice(pitch,length,True) if neon else ins.pluck(pitch,length,1850.)
                    self.note("lead",a+off*self.beat,length,pitch,.66 if neon and drop else .37 if drop else .25,
                              pan=.08 if j%2 else -.08,sound=sound,boundary=b)
            for beat in range(4):
                start=a+beat*self.beat
                if start>=b or not active:
                    continue
                if not neon or beat in (0,2):
                    self.add("drums",start,kick,.73 if drop else .48)
                    self.kicks.append(start)
                    self.events.append({"stem":"drums","time":start,"duration":.12,"note":36,"velocity":100})
                if beat%2:
                    self.add("drums",start,clap,.76 if neon else .57)
                    self.events.append({"stem":"drums","time":start,"duration":.10,"note":39,"velocity":82})
                for sub in ([.5] if neon else [.25,.5,.75] if drop else [.5]):
                    self.add("drums",start+sub*self.beat,hat,.36 if neon else .28,pan=.13 if beat%2 else -.13)
                bass_off=[0,.5] if neon else [.5,.875] if drop else [.5]
                for off in bass_off:
                    length=self.beat*(.36 if neon else .24)
                    pitch=chord["root"]+(12 if neon and beat==3 and off==.5 else 0)
                    self.note("bass",start+off*self.beat,length,pitch,.55,sound=ins.bass_note(pitch,length),boundary=b)
                if drop or role=="build":
                    for pitch in chord["voices"]:
                        length=self.beat*(.62 if neon else .32)
                        self.note("chords",start+(.25 if neon else .5)*self.beat,length,pitch+12,.18 if neon else .12,
                                  sound=neon_voice(pitch+12,length) if neon else ins.chord_voice(pitch+12,length,True),boundary=b)
            if drop and not neon or role=="build":
                for j in range(8):
                    pitch=chord["voices"][[0,2,1,2][j%4]]+12
                    length=self.beat*.23
                    self.note("arp",a+j*self.beat/2,length,pitch,.035,pan=.3 if j%2 else -.3,
                              sound=ins.pluck(pitch,length,1250),boundary=b)
        for section in self.cfg["sections"]:
            if section["role"]=="drop":
                self.add("effects",section["start"],ins.crash(),.25)
                if section["start"]>=1.5:
                    self.add("effects",section["start"]-1.5,ins.swell(1.5),.45)
        self.instrument_source="Original electronic synthesis; new "+self.cfg["music"]["style"]+" hooks and instrument arrangement"


root,cfg=load(args.project)
score=GalleryScore(root,cfg)
score.arrange()
score.audit()
score.mix()
score.write_midi(root/"outputs"/(cfg["slug"]+"-music.mid"))
print("CUSTOM_SCORE_COMPLETE",cfg["slug"],flush=True)
