# NEO Conversion Landing Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publicar uma landing page de tráfego pago da NEO orientada a cliques qualificados no WhatsApp oficial 5561998745357, com mensagem mais direta, ativos estáveis e testes objetivos antes da liberação.

**Architecture:** Manter a solução estática e sem framework, concentrando a experiência em um único `index.html` responsivo e em ativos visuais leves dentro de `images/`. A navegação será um funil curto: intenção local → sintomas → prova de capacidade → blocos de alta intenção → convênios → localização → CTA final. Toda ação primária abrirá WhatsApp com mensagem específica e `data-track` individual.

**Tech Stack:** HTML5, CSS nativo, JavaScript nativo, GitHub Pages, Python 3 (verificações estáticas locais).

**Spec:** `docs/superpowers/specs/2026-09-01-neo-conversion-landing-page-design.md`

## Global Constraints

- Objetivo primário: clique no WhatsApp oficial `5561998745357`.
- Telefone fixo permanece `(61) 3547-3607` apenas como canal secundário.
- Não usar superlativos, promessa de resultado ou alegações médicas sem comprovação.
- Não inventar CRM, RQE, diretor técnico, convênios específicos ou exames não confirmados.
- Sem frameworks ou dependências que bloqueiem renderização.
- Nenhuma imagem quebrada no deploy final.
- Hero prioritário; imagens abaixo da dobra com `loading="lazy"`.
- Todos os CTAs com `data-track` e evento `neo_cta_click` no `dataLayer`.
- Publicação final diretamente na branch `main` após testes locais.

---

### Task 1: Regression checks for conversion and asset integrity

**Files:**
- Create: `tests/verify_landing.py`
- Test: `index.html`

**Interfaces:**
- Consumes: HTML final em `index.html`.
- Produces: verificação automática que falha se número antigo, CTAs sem rastreamento, H1 inválido, placeholders ou ativos inexistentes forem introduzidos.

- [ ] **Step 1: Write the failing test**

```python
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")

assert "556135473607" not in HTML
assert "5561998745357" in HTML
assert HTML.count("<h1") == 1
assert "Otorrino na Asa Sul" in HTML
assert "data-track=" in HTML
assert "neo_cta_click" in HTML
assert "TODO" not in HTML and "TBD" not in HTML

assets = re.findall(r'(?:src|url\()[\"\']?(images/[^\"\')]+)', HTML)
missing = [asset for asset in assets if not (ROOT / asset).exists()]
assert not missing, f"Missing assets: {missing}"

print("landing checks: PASS")
```

- [ ] **Step 2: Run test to verify current build fails for the known image/deploy problem**

Run: `python tests/verify_landing.py`
Expected: FAIL while the page still references unstable/broken image assets or misses new conversion requirements.

- [ ] **Step 3: Keep the test as the release gate**

Do not weaken assertions to make an incorrect build pass.

- [ ] **Step 4: Commit**

```bash
git add tests/verify_landing.py
git commit -m "test: add NEO landing release checks"
```

### Task 2: Rebuild the conversion-focused landing page

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: copy and funnel requirements from the approved spec.
- Produces: one-page conversion funnel with unique WhatsApp intents and event tracking.

- [ ] **Step 1: Implement the new semantic structure**

Required section order:

```text
sticky conversion bar
hero
trust strip
symptom selector
consultation
high-intent blocks: dizziness + hearing
services/exams
cochlear education
insurance objection handling
NEO trust block
location
final CTA
mobile sticky WhatsApp CTA
```

- [ ] **Step 2: Implement exact conversion mechanics**

Every primary CTA must use:

```text
https://wa.me/5561998745357?text=<encoded intent-specific message>
```

Required `data-track` values include at least:

```text
whatsapp_header
whatsapp_hero
whatsapp_symptom_dizziness
whatsapp_symptom_hearing
whatsapp_symptom_ear
whatsapp_symptom_nose
whatsapp_symptom_voice
whatsapp_symptom_sleep
whatsapp_symptom_child
whatsapp_consultation
whatsapp_dizziness
whatsapp_hearing
whatsapp_cochlear
whatsapp_insurance
whatsapp_location
whatsapp_final
whatsapp_mobile_fixed
```

- [ ] **Step 3: Add compact tracking**

```javascript
document.querySelectorAll('[data-track]').forEach(function(link){
  link.addEventListener('click', function(){
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: 'neo_cta_click',
      cta: link.dataset.track,
      section: link.closest('section,header,aside')?.id || 'global',
      pathname: window.location.pathname,
      destination: link.getAttribute('href')
    });
  });
});
```

- [ ] **Step 4: Keep copy compliant and specific**

Do not include claims such as `melhor`, `maior`, `líder`, `garantido`, `resultado garantido` or invented regulatory credentials.

- [ ] **Step 5: Run static release gate**

Run: `python tests/verify_landing.py`
Expected: PASS after assets from Task 3 exist.

### Task 3: Replace unstable image delivery with safe web assets

**Files:**
- Create/replace: `images/neo-hero.svg`
- Create/replace: `images/neo-consultation.svg`
- Create/replace: `images/neo-hearing.svg`
- Create/replace: `images/neo-dizziness.svg`
- Create/replace: `images/neo-exams.svg`
- Create/replace: `images/neo-team.svg`
- Create/replace: `images/neo-location.svg`
- Modify: `index.html`

**Interfaces:**
- Consumes: visual references already supplied for the NEO page.
- Produces: deterministic UTF-8 image assets that GitHub Pages can serve without the binary truncation seen in previous JPEG uploads.

- [ ] **Step 1: Create safe SVG assets**

Each file must be valid SVG text, use a stable `viewBox`, preserve aspect ratio and contain the chosen visual treatment. If using embedded raster data, the SVG file itself must remain valid UTF-8 and be fully retrievable from GitHub.

- [ ] **Step 2: Update every image reference**

No production `img` or CSS `url()` may point to the previously corrupted `.jpg` files.

- [ ] **Step 3: Validate references locally**

Run: `python tests/verify_landing.py`
Expected: `landing checks: PASS`.

### Task 4: Mobile, accessibility and visual regression sanity checks

**Files:**
- Modify: `index.html` only if a check reveals an issue.

**Interfaces:**
- Consumes: final responsive page.
- Produces: keyboard-accessible links, readable contrast, no CTA overlap, no horizontal overflow.

- [ ] **Step 1: Verify semantics**

Check that there is exactly one H1, all images have `alt`, all external WhatsApp/map links have `target="_blank" rel="noopener"`, and interactive elements are anchors rather than non-semantic clickable divs.

- [ ] **Step 2: Verify responsive CSS breakpoints**

Required behavior:

```text
< 760px: single-column funnel, mobile sticky WhatsApp CTA visible
>= 760px: two-column content where useful, mobile sticky CTA hidden, header CTA visible
```

- [ ] **Step 3: Re-run release gate**

Run: `python tests/verify_landing.py`
Expected: PASS.

### Task 5: Publish to main and verify the public site

**Files:**
- Modify: `index.html`
- Add: safe image assets under `images/`
- Add: `tests/verify_landing.py`

**Interfaces:**
- Consumes: locally verified build.
- Produces: public GitHub Pages deployment at `https://armidiasintegradas.github.io/teste/`.

- [ ] **Step 1: Commit implementation to `main`**

Commit message:

```text
Rebuild NEO landing page for conversion
```

- [ ] **Step 2: Verify repository state**

Confirm `main` points to the new commit and `index.html` contains `5561998745357` with no `556135473607` WhatsApp links.

- [ ] **Step 3: Verify public HTML**

Open `https://armidiasintegradas.github.io/teste/` and confirm the new hero/copy is present.

- [ ] **Step 4: Verify every production asset directly**

Open each URL under `/teste/images/` used by the final HTML. A failed asset blocks completion.

- [ ] **Step 5: Verify conversion destinations**

Inspect the published HTML/links and confirm all WhatsApp CTAs target `5561998745357` with intent-specific messages; keep the fixed telephone link `tel:+556135473607` as secondary contact only.

- [ ] **Step 6: Report only evidence-backed completion**

Do not claim success until public HTML and all referenced assets have been freshly verified.
