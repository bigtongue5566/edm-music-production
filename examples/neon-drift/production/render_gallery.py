"""New circuit and neon motion studies driven by each project's actual soundtrack."""
import argparse
import math
from pathlib import Path
import sys

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("mode",choices=["preview","render"])
parser.add_argument("--project",type=Path,required=True)
args=parser.parse_args()
sys.path.insert(0,str(args.project.resolve()/"work"))
import numpy as np
from PIL import Image
import skia
from original_renderer import Film,ease,paint


class GalleryFilm(Film):
    def background(self, light):
        y,x=np.mgrid[0:self.h,0:self.w]
        neon=self.cfg["slug"]=="neon-drift"
        base=np.array([15,9,31] if neon else [5,9,24],dtype=float)
        glow=np.exp(-(((x-1400)/700)**2+((y-500)/570)**2))
        rgb=base[None,None,:]+glow[:,:,None]*np.array([39,8,39] if neon else [4,24,42])
        return skia.Image.fromarray(np.dstack((np.uint8(np.clip(rgb,0,255)),np.full((self.h,self.w),255,np.uint8))),colorType=skia.ColorType.kRGBA_8888_ColorType)

    def line(self,c,x1,y1,x2,y2,alpha=.5,width=2,accent=None):
        c.drawLine(x1,y1,x2,y2,paint(accent or self.palette["accent"],alpha,width))

    def dot(self,c,x,y,r=5,accent=None,alpha=1):
        c.drawCircle(x,y,r,paint(accent or self.palette["accent"],alpha))

    def tech(self,c,kind,t,u,level,pulse,frame):
        cx,cy=1400,535
        accent,second=self.palette["accent"],self.palette["second"]
        if kind in ("origin","circuit","matrix"):
            for row in range(7):
                for col in range(8):
                    x,y=1015+col*96,240+row*93
                    phase=(row*1.7+col*.65+t*1.6)
                    energy=.4+.6*(.5+.5*math.sin(phase))
                    if kind=="matrix":
                        energy=.15+.85*float(self.spectra[frame,(row*8+col)%32])
                    radius=(10+level*12)*energy if kind=="matrix" else 4+pulse*3
                    c.drawRoundRect(skia.Rect.MakeXYWH(x-29,y-29,58,58),7,7,paint(accent,.045+energy*.11))
                    c.drawRoundRect(skia.Rect.MakeXYWH(x-29,y-29,58,58),7,7,paint(accent,.25+energy*.4,1.5))
                    self.dot(c,x,y,radius,second if (row+col)%7==0 else accent,.65)
                    if col<7:
                        self.line(c,x+29,y,x+67,y,.19,1)
                        moving=(t*.54+row*.12+col*.21)%1
                        self.dot(c,x+31+moving*34,y,2.5,second,.8)
                    if row<6:
                        self.line(c,x,y+29,x,y+64,.11,1)
            if kind=="origin":
                self.line(c,968,185,1790,185,.42)
                self.text(c,"SIGNAL ARRAY / 08 × 07",977,165,19,accent)
        elif kind in ("scan","radar"):
            rings=7 if kind=="scan" else 4
            for ring in range(rings):
                radius=70+ring*48+(12*pulse if kind=="radar" else 0)
                c.drawCircle(cx,cy,radius,paint(accent,.12+(.22 if ring==round(t)%rings else 0),1.4))
            for i in range(64):
                angle=i*math.tau/64
                radius=350
                self.line(c,cx+math.cos(angle)*radius,cy+math.sin(angle)*radius,cx+math.cos(angle)*(radius+(18 if i%8==0 else 7)),cy+math.sin(angle)*(radius+(18 if i%8==0 else 7)),.6,1.2)
            theta=t*.48
            for j in range(16):
                angle=theta-j*.022
                self.line(c,cx,cy,cx+math.cos(angle)*335,cy+math.sin(angle)*335,(1-j/16)*.20,3)
            for i in range(12):
                angle=i*2.4+t*.10
                radius=75+(i*53)%235
                self.dot(c,cx+math.cos(angle)*radius,cy+math.sin(angle)*radius,4+level*4,second,.55+.45*math.sin(t+i)**2)
            self.dot(c,cx,cy,8+pulse*9,second)
        else:
            for row in range(18):
                points=[]
                for x in np.linspace(970,1820,100):
                    phase=(x-970)/120+t*(.7+row*.02)
                    y=240+row*32+math.sin(phase)*(20+level*27)*math.sin((x-970)/850*math.pi)
                    points.append((x,y))
                self.path(c,points,accent,.2+row/30,2)
                loc=(t*.15+row*.051)%1
                index=min(98,round(loc*99))
                self.dot(c,*points[index],3.5,second,.8)

    def neon(self,c,kind,t,u,level,pulse,frame):
        accent,second=self.palette["accent"],self.palette["second"]
        cx,cy=1400,420
        if kind in ("sunrise","road","horizon"):
            radius=205+(8*level)
            c.drawCircle(cx,cy,radius,paint(second,.92))
            for row in range(12):
                y=cy-5+row*17
                if y>cy+radius: break
                half=math.sqrt(max(0,radius**2-(y-cy)**2))
                c.drawRect(skia.Rect.MakeXYWH(cx-half,y,half*2,4+row*.52),paint("#331236",.82))
            horizon=650 if kind!="horizon" else 610
            self.line(c,960,horizon,1830,horizon,.7,2)
            for i in range(-7,8):
                self.line(c,cx+i*23,horizon,1400+i*200,925,.30,1.6)
            for i in range(12):
                z=(i/12+t*.15)%1
                y=horizon+(z**2)*(925-horizon)
                self.line(c,960,y,1830,y,.13+.38*z,1.2)
            for i in range(7):
                x=1050+i*120+math.sin(t*.2+i)*15
                self.dot(c,x,190+math.sin(t*.16+i)*34,2.4,second,.6)
        elif kind=="ribbons":
            for row in range(25):
                points=[]
                for x in np.linspace(960,1840,110):
                    wave=(x-960)/160+t*.7+row*.10
                    points.append((x,270+row*17+math.sin(wave)*(90+level*40)))
                self.path(c,points,second if row%6==0 else accent,.16+.65*row/25,2.4 if row%6==0 else 1.6)
            for i in range(4):
                angle=t*.5+i*math.pi/2
                self.dot(c,cx+math.cos(angle)*200,530+math.sin(angle)*230,9+pulse*4,second,.8)
        elif kind=="city":
            for depth in range(2):
                for i in range(13):
                    x=965+i*68+depth*24
                    height=75+((i*37+depth*109)%220)+self.spectra[frame,(i*2+depth)%32]*50
                    bottom=815-depth*100
                    c.drawRect(skia.Rect.MakeXYWH(x,bottom-height,47,height),paint(accent,.07 if depth else .12))
                    c.drawRect(skia.Rect.MakeXYWH(x,bottom-height,47,height),paint(second if i%4==0 else accent,.24 if depth else .58,1.4))
                    for row in range(6):
                        y=bottom-24-row*33
                        if y<bottom-height+15:break
                        self.line(c,x+12,y,x+35,y,.3+.3*math.sin(t*1.4+i+row)**2,2,second)
            for row in range(10):
                y=850+row*7
                self.line(c,955,y,1830,y,.12+row*.025,1)
            for i in range(20):
                x=965+(i*121+t*45)%870
                y=210+(i*67)%160
                self.line(c,x,y,x+22,y,.38,2,second)

    def scene(self,c,scene,t,frame):
        c.drawImage(self.backgrounds[False],0,0)
        u=t-scene["start"]
        level=float(min(1,self.levels[frame]))
        role=next((s["role"] for s in self.cfg["sections"] if t<s["end"]),"outro")
        pulse=math.exp(-((t/self.beat)%1)*8) if role in ("drop","build","groove") else 0
        accent,second,fg=self.palette["accent"],self.palette["second"],self.palette["text"]
        cn=self.cfg["name"].split(" — ")[0]
        self.text(c,"ORIGINAL MOTION / ORIGINAL MUSIC",104,80,19,accent,.8)
        self.text(c,f"60 SEC / {self.cfg['music']['bpm']:g} BPM",1510,80,20,fg,.65)
        self.text(c,cn,104,987,22,fg,.85)
        self.text(c,self.cfg["music"]["style"].upper(),1310,987,18,accent,.9,width=505)
        self.line(c,104,1030,1816,1030,.13,2)
        self.line(c,104,1030,104+t/self.duration*1712,1030,.9,3)
        if scene["kind"]=="closing":
            c.save();c.translate(-440,-215);c.scale(1,1)
            if self.cfg["slug"]=="digital-pulse":self.tech(c,"radar",t,u,level,pulse,frame)
            else:self.neon(c,"horizon",t,u,level,pulse,frame)
            c.restore()
            # A dark panel leaves a clean end title while geometry keeps moving above it.
            c.drawRect(skia.Rect.MakeXYWH(0,530,1920,420),paint(self.palette["background"],.97))
            self.text(c,scene["headline"],960,660,109,fg,ease(u/.7),center=True,bold=True)
            self.text(c,scene["caption"],960,760,50,accent,ease((u-.2)/.6),center=True)
            self.text(c,scene["body"],960,845,22,second,ease((u-.45)/.6),center=True)
            return
        self.text(c,f"{self.scenes.index(scene)+1:02d} / {scene['caption']}",104,244,22,accent,ease(u/.7),width=820)
        self.text(c,scene["headline"],104,408+(1-ease(u/.8))*26,112 if scene["kind"] in ("origin","sunrise") else 91,fg,ease(u/.8),width=810,bold=True)
        self.text(c,scene["caption"],104,741,40,second,ease((u-.2)/.7),width=820)
        self.text(c,scene["body"],104,812,27,fg,ease((u-.4)/.7),width=790)
        c.save();c.clipRect(skia.Rect.MakeXYWH(940,130,925,790))
        if self.cfg["slug"]=="digital-pulse":self.tech(c,scene["kind"],t,u,level,pulse,frame)
        else:self.neon(c,scene["kind"],t,u,level,pulse,frame)
        c.restore()

    def preview(self):
        board=Image.new("RGB",(1920,1080),self.palette["background"])
        for i,scene in enumerate(self.scenes):
            time=scene["start"]+min(2.5,(scene["end"]-scene["start"])/2)
            pic=Image.fromarray(self.frame(round(time*self.fps))).convert("RGB")
            pic.save(self.root/"work"/f"preview-{i:02d}.jpg",quality=94)
            board.paste(pic.resize((640,360),Image.Resampling.LANCZOS),((i%3)*640,(i//3)*360))
        board.save(self.root/"outputs"/(self.cfg["slug"]+"-storyboard.jpg"),quality=94)
        Image.fromarray(self.frame(round(4*self.fps))).convert("RGB").save(self.root/"outputs"/(self.cfg["slug"]+"-poster.jpg"),quality=95)
        print("NEW_DEMO_PREVIEW_READY",self.cfg["slug"],flush=True)


film=GalleryFilm(args.project)
getattr(film,args.mode)()
