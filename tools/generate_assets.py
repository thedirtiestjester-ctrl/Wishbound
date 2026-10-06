from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math, random

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / 'game' / 'images'
GUI = ROOT / 'game' / 'gui'
IMG.mkdir(parents=True, exist_ok=True)
GUI.mkdir(parents=True, exist_ok=True)

W,H=1280,720

def font(size=42):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf']:
        if Path(p).exists(): return ImageFont.truetype(p,size)
    return ImageFont.load_default()

def gradient(size, top, bottom):
    w,h=size
    im=Image.new('RGB',size)
    px=im.load()
    for y in range(h):
        t=y/max(1,h-1)
        c=tuple(int(top[i]*(1-t)+bottom[i]*t) for i in range(3))
        for x in range(w): px[x,y]=c
    return im

def label_bg(name,title,top,bottom,accent=(232,180,255)):
    im=gradient((W,H),top,bottom); d=ImageDraw.Draw(im,'RGBA')
    # window / horizon geometry
    d.rounded_rectangle((70,75,1210,645), radius=36, fill=(8,10,24,92), outline=accent+(120,), width=4)
    d.rectangle((0,520,W,H), fill=(6,7,16,115))
    d.ellipse((880,80,1130,330), fill=accent+(35,))
    d.text((80,80),title,font=font(48),fill=(250,247,255,235))
    d.text((82,142),'WISHBOUND • PLACEHOLDER LOCATION ART',font=font(20),fill=accent+(220,))
    # depth lines
    for i in range(6):
        y=250+i*55; d.line((110,y,1170,y),fill=(255,255,255,20),width=2)
    im.save(IMG/name,optimize=True)

backgrounds={
'bg_bedroom.png':('Claire’s Bedroom',(52,34,76),(18,18,34),(231,149,255)),
'bg_bathroom.png':('Bathroom / Mirror',(35,67,84),(13,25,37),(147,226,255)),
'bg_cafe.png':('Corner Café',(85,55,38),(28,20,24),(255,201,145)),
'bg_city.png':('Downtown',(34,41,76),(12,14,31),(154,174,255)),
'bg_closet.png':('Closet',(75,39,67),(25,18,32),(255,151,202)),
'bg_event_venue.png':('Event Venue',(61,35,92),(16,14,31),(219,169,255)),
'bg_kitchen.png':('Kitchen',(62,58,67),(19,23,30),(232,214,176)),
'bg_office_lobby.png':('Office Lobby',(32,56,76),(11,18,30),(141,207,255)),
'bg_phone.png':('Phone / Digital History',(38,33,68),(12,11,28),(179,159,255)),
'bg_photo_studio.png':('Photo Studio',(66,54,73),(17,16,24),(255,214,234)),
'bg_rooftop_club.png':('Halo Roof',(40,25,73),(8,9,25),(223,123,255)),
'bg_tattoo_studio.png':('Crossline Studio',(47,42,43),(14,14,17),(242,166,118)),
'bg_void.png':('The Wish',(18,9,36),(2,2,10),(206,122,255)),
'bg_title.png':('WISHBOUND: HER MORNING',(45,20,72),(8,8,19),(229,135,255)),
}
for fn,(title,top,bottom,accent) in backgrounds.items(): label_bg(fn,title,top,bottom,accent)

# wish effect overlay
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im,'RGBA'); random.seed(42)
for r,a in [(310,20),(220,32),(150,46),(90,70)]: d.ellipse((W//2-r,H//2-r,W//2+r,H//2+r),outline=(229,154,255,a),width=7)
for i in range(120):
    x=random.randrange(W); y=random.randrange(H); rr=random.choice([1,1,2,3]); d.ellipse((x-rr,y-rr,x+rr,y+rr),fill=(240,208,255,random.randrange(40,150)))
im.save(IMG/'fx_wish.png',optimize=True)

sprites={
'sprite_mia_hart.png':('MIA HART',(122,65,104),(240,179,211),'28'),
'sprite_avery_lane.png':('AVERY LANE',(53,74,119),(187,214,255),'30'),
'sprite_chloe_vale.png':('CHLOE VALE',(105,74,42),(244,207,169),'25'),
'sprite_naomi_cross.png':('NAOMI CROSS',(48,53,56),(224,176,143),'33'),
'sprite_lila_morgan.png':('LILA MORGAN',(71,50,84),(223,179,211),'26'),
'sprite_rhea_park.png':('RHEA PARK',(48,31,82),(210,169,239),'29'),
}
for fn,(name,outfit,skin,age) in sprites.items():
    size=(700,900) if 'naomi' in fn or 'lila' in fn or 'rhea' in fn else (540,680)
    w,h=size; im=Image.new('RGBA',size,(0,0,0,0)); d=ImageDraw.Draw(im,'RGBA')
    # soft shadow
    d.ellipse((w*.23,h*.88,w*.77,h*.96),fill=(0,0,0,65))
    # legs/body/head stylized dress-form silhouette
    d.rounded_rectangle((w*.39,h*.56,w*.49,h*.89),20,fill=outfit+(255,)); d.rounded_rectangle((w*.51,h*.56,w*.61,h*.89),20,fill=outfit+(255,))
    d.rounded_rectangle((w*.29,h*.28,w*.71,h*.68),int(w*.14),fill=outfit+(255,),outline=(255,255,255,70),width=3)
    d.ellipse((w*.34,h*.06,w*.66,h*.36),fill=skin+(255,),outline=(255,255,255,65),width=3)
    # hair + eyes
    hair=tuple(max(10,c-55) for c in outfit); d.pieslice((w*.31,h*.025,w*.69,h*.38),180,360,fill=hair+(255,))
    eyey=h*.19; d.ellipse((w*.425,eyey,w*.45,eyey+10),fill=(32,25,38,230)); d.ellipse((w*.55,eyey,w*.575,eyey+10),fill=(32,25,38,230))
    d.arc((w*.46,h*.215,w*.54,h*.255),0,180,fill=(120,45,70,220),width=3)
    d.rounded_rectangle((18,h-105,w-18,h-18),24,fill=(10,10,21,205),outline=(255,255,255,45),width=2)
    d.text((35,h-92),name,font=font(int(w*.058)),fill=(255,255,255,245))
    d.text((35,h-52),f'AGE {age} • REWRITTEN IDENTITY',font=font(int(w*.028)),fill=(232,198,255,225))
    im.save(IMG/fn,optimize=True)

# GUI assets
im=Image.new('RGBA',(500,80),(30,24,47,228)); d=ImageDraw.Draw(im,'RGBA'); d.rounded_rectangle((1,1,498,78),20,outline=(227,149,255,180),width=3); im.save(GUI/'button.png',optimize=True)
im=Image.new('RGBA',(1280,220),(9,9,18,215)); d=ImageDraw.Draw(im,'RGBA'); d.rectangle((0,0,1280,4),fill=(220,145,255,180)); im.save(GUI/'textbox.png',optimize=True)
print('Generated', len(backgrounds)+1+len(sprites)+2, 'PNG assets')
