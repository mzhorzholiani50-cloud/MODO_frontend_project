from pathlib import Path
import math, random, html
root=Path(__file__).parent
specs=[
 ('ORBIT','FIELD','153D35','D6FB68','F4F2E9','orbit'),
 ('KINETIC','TYPE','F06C56','2B2523','FFEBD6','type'),
 ('BLOOM','CLUB','C9BDF8','372B67','E7FD9D','flowers'),
 ('IN / OUT','SPACE','EED1A9','E66B4D','222B2A','arch'),
 ('ECHO','WAVES','9FE1D5','16484B','F7F0E7','waves'),
 ('SOFT','FORM','F8D4D7','BC405C','F5F1ED','circles'),
 ('MONO','STUDIO','D5DFE4','1B2429','FEFAF3','lines'),
 ('AFTER','IMAGE','1D2633','DDFF6B','E6D8EB','stars'),
 ('NEW','RITUAL','F1B18A','683B3D','F6E6C0','arch'),
 ('OFF','GRID','D6F8B1','163F45','FF6C51','grid'),
 ('SLOW','MOTION','C7CEFC','273B90','FFF8F0','waves'),
 ('OTHER','SIDE','EEE6DB','3F4A3D','E2F171','circles')]
def svg_for(i,s):
 name,sub,bg,fg,accent,kind=s
 bg='#'+bg; fg='#'+fg; ac='#'+accent
 rng=random.Random(i)
 stuff=[]
 if kind=='orbit':
  for r in range(280,30,-48):
   stuff.append(f'<circle cx="400" cy="408" r="{r}" fill="none" stroke="{fg if r%2 else ac}" stroke-width="16" opacity=".95"/>')
  stuff.append(f'<circle cx="402" cy="410" r="84" fill="{ac}"/>')
 if kind=='type':
  for j in range(7):
   y=118+j*110
   stuff.append(f'<text x="{-50 if j%2 else 60}" y="{y}" font-size="142" font-weight="900" letter-spacing="-12" fill="{fg}" opacity="{.2+j*.09:.2f}" transform="skewY(-10)">Aa Aa Aa</text>')
 if kind=='flowers':
  for x,y,scale in [(250,260,1.0),(580,330,.73),(400,605,1.14)]:
   for j in range(8):
    a=j*math.pi/4
    cx=x+math.cos(a)*84*scale;cy=y+math.sin(a)*84*scale
    stuff.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{38*scale:.1f}" ry="{85*scale:.1f}" fill="{fg}" transform="rotate({j*45} {cx:.1f} {cy:.1f})"/>')
   stuff.append(f'<circle cx="{x}" cy="{y}" r="{52*scale:.1f}" fill="{ac}"/>')
 if kind=='arch':
  for j in range(6):
   x=-110+j*165
   stuff.append(f'<path d="M {x} 665 L {x} 320 A 82 82 0 0 1 {x+164} 320 L {x+164} 665 Z" fill="none" stroke="{fg}" stroke-width="23" opacity="{1-j*.08:.2f}"/>')
 if kind=='waves':
  for j in range(20):
   y=100+j*27
   amp=75+j*2
   d=f'M -30 {y}'
   for x in range(-30,901,110):
    d+=f' Q {x+55} {y-amp if (x//110)%2==0 else y+amp} {x+110} {y}'
   stuff.append(f'<path d="{d}" stroke="{fg}" fill="none" stroke-width="6" opacity="{1-j*.027:.2f}"/>')
 if kind=='circles':
  for j in range(9):
   x=160+(j%3)*245;y=155+(j//3)*240
   stuff.append(f'<circle cx="{x}" cy="{y}" r="{88+(j%2)*21}" fill="{fg if j%2 else ac}" opacity=".94"/>')
 if kind=='lines':
  for j in range(29):
   x=25+j*31
   stuff.append(f'<path d="M {x} -20 L {x+270} 930" stroke="{fg}" stroke-width="{2+(j%4)*2}" opacity=".77"/>')
  stuff.append(f'<circle cx="430" cy="405" r="192" fill="{ac}" opacity=".88"/>')
 if kind=='stars':
  for j in range(31):
   x=rng.randint(10,790);y=rng.randint(10,850);r=rng.randint(7,40)
   stuff.append(f'<path d="M {x} {y-r} L {x+r//4} {y-r//4} L {x+r} {y} L {x+r//4} {y+r//4} L {x} {y+r} L {x-r//4} {y+r//4} L {x-r} {y} L {x-r//4} {y-r//4} Z" fill="{fg}"/>')
 if kind=='grid':
  for x in range(0,830,60): stuff.append(f'<path d="M {x} 0 V 900" stroke="{fg}" stroke-width="2" opacity=".34"/>')
  for y in range(0,930,60): stuff.append(f'<path d="M 0 {y} H 800" stroke="{fg}" stroke-width="2" opacity=".34"/>')
  stuff.append(f'<circle cx="410" cy="390" r="195" fill="{ac}"/>')
  stuff.append(f'<rect x="300" y="270" width="230" height="230" fill="{fg}" transform="rotate(21 410 390)"/>')
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="900" viewBox="0 0 800 900" role="img" aria-label="Abstract poster: {html.escape(name)}"><rect width="800" height="900" fill="{bg}"/><g>{''.join(stuff)}</g><rect x="0" y="724" width="800" height="176" fill="{bg}" opacity=".95"/><path d="M 48 727 H 752" stroke="{fg}" opacity=".45"/><text x="49" y="794" font-family="Arial,Helvetica,sans-serif" font-size="82" letter-spacing="-5" font-weight="900" fill="{fg}">{html.escape(name)}</text><text x="52" y="844" font-family="Arial,Helvetica,sans-serif" font-size="22" letter-spacing="9" font-weight="600" fill="{fg}">{html.escape(sub)} · 2026</text><circle cx="722" cy="825" r="20" fill="{ac}"/></svg>'''
 return svg
for n,s in enumerate(specs,1):
 (root/'assets'/'posters'/f'{n:02d}.svg').write_text(svg_for(n,s),encoding='utf-8')
(root/'assets'/'favicon.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="15" fill="#18392d"/><path d="M12 46V18h10l10 14 10-14h10v28H42V31L32 44 22 31v15z" fill="#dcf879"/></svg>''',encoding='utf-8')
print('Created posters')
