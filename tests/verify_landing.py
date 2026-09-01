from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, parse_qs
import re
import xml.etree.ElementTree as ET
import base64, io
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
HTML=(ROOT/'index.html').read_text(encoding='utf-8')

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.h1=0; self.images=[]; self.links=[]; self.ids=set(); self.body_depth=0; self.body_children=[]; self.forbidden_layout=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='body': self.body_depth=1; return
        if self.body_depth==1: self.body_children.append((tag,d))
        if self.body_depth: self.body_depth+=1
        if tag in {'header','footer'}: self.forbidden_layout.append(tag)
        if tag=='h1': self.h1+=1
        if tag=='img': self.images.append(d)
        if tag=='a': self.links.append(d)
        if 'id' in d: self.ids.add(d['id'])
    def handle_endtag(self,tag):
        if self.body_depth: self.body_depth-=1

p=P(); p.feed(HTML)
assert p.h1==1
assert not p.forbidden_layout, f'Elementos de layout proibidos: {p.forbidden_layout}'
assert p.body_children[0][0]=='main' and p.body_children[0][1].get('id')=='inicio'
assert 'header{' not in HTML and 'header ' not in HTML and 'footer{' not in HTML
assert re.search(r'img\{[^}]*height:auto', HTML), 'Imagens responsivas precisam preservar a proporção natural'
assert 'Otorrino na Asa Sul' in HTML
assert '556135473607?text=' not in HTML
assert 'wa.me/5561998745357' in HTML
assert 'neo_cta_click' in HTML and 'data-track' in HTML
assert 'TODO' not in HTML and 'TBD' not in HTML
for forbidden in ['líder absoluto','maiores especialistas','maior especialista','resultado garantido']:
    assert forbidden not in HTML.lower()
required={'whatsapp_hero','whatsapp_symptom_dizziness','whatsapp_symptom_hearing','whatsapp_symptom_ear','whatsapp_symptom_nose','whatsapp_symptom_voice','whatsapp_symptom_sleep','whatsapp_symptom_child','whatsapp_consultation','whatsapp_dizziness','whatsapp_hearing','whatsapp_cochlear','whatsapp_insurance','whatsapp_location','whatsapp_final','whatsapp_mobile_fixed'}
tracks=set(re.findall(r'data-track="([^"]+)"',HTML)); assert not(required-tracks)
wa=[a for a in p.links if a.get('href','').startswith('https://wa.me/')]
assert len(wa)>=16
for a in wa:
    href=a['href']; assert href.startswith('https://wa.me/5561998745357?text=')
    assert parse_qs(urlparse(href).query).get('text')
    assert a.get('target')=='_blank' and 'noopener' in a.get('rel','')
assert any(a.get('href')=='tel:+556135473607' for a in p.links)
assert any('google.com/maps' in a.get('href','') for a in p.links)
for img in p.images:
    src=img.get('src'); path=ROOT/src
    assert src.startswith('images/') and path.exists() and img.get('alt','').strip()
    if path.suffix=='.svg':
        ET.parse(path)
        text=path.read_text(encoding='utf-8')
        m=re.search(r'data:image/jpeg;base64,([^\"\']+)', text)
        assert m, f'JPEG incorporado ausente em {src}'
        raw=base64.b64decode(m.group(1), validate=True)
        im=Image.open(io.BytesIO(raw)); im.verify()
        im=Image.open(io.BytesIO(raw))
    else:
        im=Image.open(path); im.verify(); im=Image.open(path)
    assert im.width>=1600 and im.height>=900, f'Imagem sem alta resolução: {src} ({im.width}x{im.height})'
for ref in re.findall(r'href="#([^"]+)"',HTML): assert ref in p.ids
print(f'landing checks: PASS | {len(p.images)} imagens | {len(wa)} CTAs WhatsApp')
