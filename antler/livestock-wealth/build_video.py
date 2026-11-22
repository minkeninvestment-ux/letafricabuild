#!/usr/bin/env python3
"""Generate Antler Kenya concept pitch: synthetic narration, no founder impersonation."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import subprocess
P=Path(__file__).parent;tmp=P/'build';tmp.mkdir(exist_ok=True)
out=P/'minken_antler_livestock_pitch.mp4'
S=[
("Livestock wealth, unlocked.","Better animal health. Better connections. Better markets.","Introducing Minken Livestock Wealth, a platform concept led by Hukun Dabar, founder of Minken Africa in Nairobi. Our goal is to help livestock owners access the services and connections they need to grow."),
("The problem: fragmentation.","Critical services are not always easy to find.","For many livestock owners, finding a trusted veterinary professional, reaching serious buyers, and obtaining timely market information can involve separate networks and costly delays. We want to bring these connections together."),
("One connected platform.","Mobile-first livestock services marketplace.","Our proposed platform brings together veterinary bookings, livestock market discovery, and practical herd-support tools. Farmers and pastoralists can find service providers, explore buyer interest, and make more informed decisions from one place."),
("Built around a real journey.","Discover  /  Connect  /  Get support  /  Follow up","Imagine a livestock owner locating a qualified vet, arranging a visit, finding relevant buyers, and keeping useful animal-care reminders in one simple experience. These are workflows we want to validate with real users."),
("Validate before we scale.","Kenya pilot → learning → product refinement","We plan to begin in Kenya, speaking with livestock owners, veterinary professionals, and potential buyers. Then we will prototype, test service delivery, and measure repeat use. Our strategy is to learn before scaling."),
("Build with Antler.","Kenya first. East African potential.","Antler's Founder Residency offers a chance to sharpen our business model, build the right team, and test a scalable venture. Minken Livestock Wealth: healthier herds, stronger markets, and more connected rural economies.")
]
def F(z,b=False):
 p='/usr/share/fonts/truetype/dejavu/DejaVuSans'+('-Bold' if b else '')+'.ttf'
 return ImageFont.truetype(p,z)
for i,(a,b,narration) in enumerate(S):
 im=Image.new('RGB',(1280,720),'#071E2B');d=ImageDraw.Draw(im)
 d.ellipse((880,-200,1500,450),fill='#0C3344')
 d.rounded_rectangle((65,48,300,97),radius=20,fill='#154052')
 d.text((82,59),'MINKEN AFRICA',font=F(22,True),fill='#6BE7CA')
 d.text((65,150),a,font=F(48,True),fill='#FFFFFF')
 d.text((65,238),b,font=F(25),fill='#B6CDD4')
 d.rounded_rectangle((65,320,1200,585),radius=30,fill='#123447')
 for j,(label,symbol) in enumerate([('LIVESTOCK OWNERS','01'),('VETERINARY CARE','02'),('TRUSTED MARKETS','03')]):
  x=102+j*365
  d.ellipse((x,365,x+75,440),fill='#6BE7CA')
  d.text((x+16,382),symbol,font=F(23,True),fill='#071E2B')
  d.text((x,480),label,font=F(19,True),fill='#FFFFFF')
 d.text((65,650),'EARLY-STAGE CONCEPT  •  NOT AN MVP DEMONSTRATION',font=F(17),fill='#B6CDD4')
 d.text((1050,650),f'{i+1} / 6',font=F(19),fill='#6BE7CA')
 im.save(tmp/f'{i:02}.png')
 subprocess.run(['espeak','-v','en-us+m3','-s','165','-a','150','-w',str(tmp/f'{i:02}.wav'),narration],check=True)
durations=[]
for i in range(len(S)):
 p=subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(tmp/f'{i:02}.wav')],text=True)
 durations.append(float(p)+0.5)
with (tmp/'video.txt').open('w') as f:
 for i,x in enumerate(durations):
  f.write("file '"+str((tmp/f'{i:02}.png').resolve())+"'\n")
  f.write(f'duration {x:.3f}\n')
 f.write("file '"+str((tmp/'05.png').resolve())+"'\n")
with (tmp/'audio.txt').open('w') as f:
 for i in range(len(S)):f.write("file '"+str((tmp/f'{i:02}.wav').resolve())+"'\n")
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(tmp/'audio.txt'),'-c:a','pcm_s16le',str(tmp/'voice.wav')],check=True)
# Match video and audio to exactly 59 seconds.
duration=sum(durations)
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(tmp/'video.txt'),'-i',str(tmp/'voice.wav'),'-vf',f'fps=24,setpts=PTS*{59/duration:.6f},format=yuv420p','-af',f'atempo={duration/59:.6f},apad','-t','59','-r','24','-c:v','libx264','-preset','ultrafast','-crf','27','-c:a','aac','-b:a','96k','-movflags','+faststart',str(out)],check=True)
print(out)
