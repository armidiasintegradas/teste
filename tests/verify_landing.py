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
        super().__init__(); self.h1=0; self.images=[]; self.links=[]; self.ids=set()
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='h1': self.h1+=1
        if tag=='img': self.images.append(d)
        if tag=='a': self.links.append(d)
        if 'id' in d: self.ids.add(d['id'])

p=P(); p.feed(HTML)
assert p.h1==1
assert 'Otorrino na Asa Sul' in HTML
assert '556135473607?text=' not in HTML
assert 'wa.me/5561998745357' in HTML
assert 'neo_cta_click' in HTML and 'data-track' in HTML
assert 'TODO' not in HTML and 'TBD' not in HTML
for forbidden in ['líder absoluto','maiores especialistas','maior especialista','resultado garantido']:
    assert forbidden not in HTML.lower()
required={'whatsapp_header','whatsapp_hero','whatsapp_symptom_dizziness','whatsapp_symptom_hearing','whatsapp_symptom_ear','whatsapp_symptom_nose','whatsapp_symptom_voice','whatsapp_symptom_sleep','whatsapp_symptom_child','whatsapp_consultation','whatsapp_dizziness','whatsapp_hearing','whatsapp_cochlear','whatsapp_insurance','whatsapp_location','whatsapp_final','whatsapp_mobile_fixed'}
tracks=set(re.findall(r'data-track="([^"]+)"',HTML)); assert not(required-tracks)
wa=[a for a in p.links if a.get('href','').startswith('https://wa.me/')]
assert len(wa)>=17
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
for ref in re.findall(r'href="#([^"]+)"',HTML): assert ref in p.ids
print(f'landing checks: PASS | {len(p.images)} imagens | {len(wa)} CTAs WhatsApp')
