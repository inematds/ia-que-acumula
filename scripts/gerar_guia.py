#!/usr/bin/env python3
"""Gera PT/EN/ES com o CSS do template INEMA; não chama modelos ou APIs."""
from pathlib import Path
import json,re,html,shutil
ROOT=Path(__file__).resolve().parent.parent
URL='https://inematds.github.io/ia-que-acumula/guia/'
REPO='https://github.com/inematds/ia-que-acumula'
ZIP=REPO+'/archive/refs/heads/main.zip'
E=lambda x:html.escape(str(x),quote=True)
css=(ROOT/'scripts/template-base.css').read_text()
extra='''
.reading{max-width:74ch}.wide{width:100%;height:auto;display:block;border-radius:14px;margin:26px 0 0}.techhead{background:var(--bg2);border-top:2px solid var(--amb);padding:48px 0}.techzone{background:var(--bg2)}.techzone section:last-child{border-bottom:0}.videos{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px 20px}.video-card{min-width:0}.video-card h3{font-size:1.04rem;line-height:1.4;margin:12px 0 8px}.video-card p{font-size:.86rem;color:var(--mut);margin:8px 0}.video-card a{text-decoration:underline;text-underline-offset:3px}.player{aspect-ratio:16/9;position:relative;background:var(--bg2);border:1px solid var(--line);overflow:hidden;border-radius:12px}.player iframe{width:100%;height:100%;border:0;display:block}.play{border:0;background:transparent;width:100%;height:100%;padding:0;cursor:pointer;position:relative;display:block;color:var(--txt)}.play img{width:100%;height:100%;object-fit:cover;display:block}.play svg{position:absolute;left:calc(50% - 28px);top:calc(50% - 28px);width:56px;height:56px;filter:drop-shadow(0 3px 9px #0009)}.round{margin:36px 0 22px;font-size:1.3rem}.sim{margin:26px 0 0;padding:26px;background:var(--bg2);border:1px solid var(--line);border-radius:14px}.sim ul{padding-left:22px}.sim li{margin:12px 0}.sim button{border:1px solid var(--line);cursor:pointer;font:inherit}.sim .agent{display:inline-block;margin-left:14px;font-family:Sora,sans-serif;font-weight:700}.flow .arr{background:transparent}.techhead h2{margin:12px 0}.round-note{max-width:74ch}.source-links{display:flex;flex-wrap:wrap;gap:18px;margin-top:24px}a:focus-visible,button:focus-visible{outline:3px solid var(--sky);outline-offset:4px}section,header,.techhead{scroll-margin-top:100px}figure{margin:22px 0}figure img{max-width:100%;height:auto}.skip{position:absolute;left:14px;top:-100px;z-index:99;background:var(--amb);color:var(--bg);padding:10px}.skip:focus{top:8px}nav .brand{max-width:180px;line-height:1.2;font-size:.92rem}.reading p{margin:1em 0}.banner-grade{width:100%;height:auto;margin-top:28px;border-radius:14px}.graph figcaption{color:var(--mut);max-width:74ch;margin-top:14px}.video-language{font-size:.8rem}.clip-link{display:inline-block;margin-top:6px}body.light nav{background:var(--bg)}.brand svg{flex:0 0 20px;width:20px;height:20px}@media(max-width:940px){.videos{grid-template-columns:1fr 1fr}}@media(max-width:600px){.videos{grid-template-columns:1fr}.hero h1{font-size:2.2rem}.sim{padding:18px}section{padding:42px 0}.phase{flex-wrap:wrap}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important;animation:none!important}}
'''
items=json.loads((ROOT/'videos.json').read_text())
for lang in ['pt','en','es']:
 t=json.loads((ROOT/'i18n'/f'{lang}.json').read_text());target=ROOT/'guia' if lang=='pt' else ROOT/'guia'/lang;target.mkdir(parents=True,exist_ok=True)
 a='assets/' if lang=='pt' else '../assets/';doc='../' if lang=='pt' else '../../';suffix='' if lang=='pt' else '-'+lang
 switchlinks={'pt':('./','en/','es/'),'en':('../','./','../es/'),'es':('../','../en/','./')}[lang]
 langlinks=''.join(f'<a href="{href}" lang="{code}"'+(' class="on" aria-current="page"' if code==lang else '')+f'>{code.upper()}</a>' for code,href in zip(['pt','en','es'],switchlinks))
 def text(key):return E(t[key])
 def fig(name,alt):return f'<img class="wide" src="{a}{name}" alt="{E(alt)}" width="1400" height="788" loading="lazy">'
 def step(n,title,body,command=''):
  return f'<div class="step"><div class="b">{n}</div><div><h3>{text(title)}</h3><p>{text(body)}</p>'+(f'<pre><code>{E(command)}</code></pre>' if command else '')+'</div></div>'
 cards=[]
 for i,it in enumerate(items):
  pub=it;vid=pub['id'];assert re.fullmatch('[A-Za-z0-9_-]{11}',vid)
  title=t['videoTitles'][i];profile={'lives11':'channelStrategic','lives7':'channelAgents','lives3':'channelBeginner'}[it['canal']]
  cards.append(f'''<article class="video-card" data-video-id="{vid}"><div class="player"><button class="play" type="button" data-play="{vid}" aria-label="{text('loadVideo')}: {E(title)}"><img src="{a}video-{it['key']}.jpg" alt="" width="640" height="360" loading="lazy"><svg viewBox="0 0 56 56" aria-hidden="true"><circle cx="28" cy="28" r="27" fill="#0c0c10" stroke="#E2A23B" stroke-width="2"/><path d="M23 17L40 28 23 39Z" fill="#E2A23B"/></svg></button></div><p>{it['canal'].upper()} · {text(profile)}</p><h3>{E(title)}</h3><p class="video-language">{text('videoLanguage')}</p><a href="{E(pub['url'])}" target="_blank" rel="noopener">{text('watch')}</a></article>''')
 icon='<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="m3 7 9-4 9 4-9 4-9-4Zm0 5 9 4 9-4M3 17l9 4 9-4"/></svg>'
 body=f'''<a class="skip" href="#resumo">{text('summaryTitle')}</a><nav><div class="wrap"><a class="brand" href="#top">{icon}{text('name')}</a><span class="sep">|</span><span class="clubpro"><a class="inema" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a><span class="sep">−</span><a class="pro" href="https://inema.pro" target="_blank" rel="noopener">PRO</a></span><div class="links"><a class="sec" href="#video">{text('navVideo')}</a><a class="sec" href="#metodo">{text('navMethod')}</a><a class="sec" href="#tecnico">{text('navKit')}</a><span class="lang" aria-label="Language">{langlinks}</span><button class="tgl" id="theme" type="button" aria-label="{text('theme')}">☀</button><a class="btn" href="{REPO}" target="_blank" rel="noopener">GitHub</a></div></div></nav>
<main id="top"><header class="hero"><div class="wrap"><div><h1><span class="amb">{text('name')}.</span><br>{text('hero')}</h1><p class="lead">{text('lead')}</p><div class="cta"><a class="btn" href="#video">{text('understand')}</a><a class="btn ghost" href="{ZIP}">{text('download')}</a></div></div><figure><img src="{a}banner{suffix}.jpg" alt="{text('bannerSub')}" width="1400" height="788" fetchpriority="high"></figure></div></header>
<section id="resumo" class="resumo"><div class="wrap"><h2>{text('summaryTitle')}</h2><p>{text('summary')}</p><img class="banner-grade" src="{a}banner-grade{suffix}.jpg" alt="{text('gradeTitle')}" width="1400" height="788" loading="lazy"></div></section>
<section id="video"><div class="wrap"><h2>{text('videoTitle')}</h2><p class="sub">{text('videoIntro')}</p><h3 class="round">{text('round1')}</h3><div class="videos">{''.join(cards[:3])}</div><h3 class="round">{text('round2')}</h3><p class="sub round-note">{text('round2Note')}</p><div class="videos">{''.join(cards[3:])}</div></div></section>
<section id="metodo"><div class="wrap"><h2>{text('methodTitle')}</h2><p class="sub">{text('methodIntro')}</p><div class="sim"><h3>{text('simulationTitle')}</h3><ul><li><strong>{text('contextLabel')}</strong> — {text('contextDetail')}</li><li><strong>{text('toolLabel')}</strong> — {text('toolDetail')}</li><li><strong>{text('proofLabel')}</strong> — {text('proofDetail')}</li></ul><button class="btn ghost" id="switch-agent" type="button">{text('switchAgent')}</button><span class="agent" id="agent-name" role="status">{text('agentA')}</span><p class="mut reading">{text('simulationNote')}</p></div></div></section>
<section id="aceleracao"><div class="wrap"><h2>{text('graphTitle')}</h2><figure class="graph">{fig('grafico-ia-exponencial.jpg',t['graphAlt'])}<figcaption>{text('graphNote')}</figcaption></figure></div></section>
<section id="plano"><div class="wrap"><h2>{text('actionTitle')}</h2><p class="sub">{text('actionIntro')}</p><div class="grid g3">'''+''.join(f'<div class="card"><h3>{text("action"+str(i)+"Title")}</h3><p>{text("action"+str(i)+"Text")}</p></div>' for i in [1,2,3])+f'''</div><div class="reading"><h3 style="margin-top:34px">{text('enterpriseTitle')}</h3><p>{text('enterpriseText')}</p></div></div></section>
<div id="tecnico" class="techhead"><div class="wrap"><span class="chip">{text('technicalLabel')}</span><h2>{text('technicalTitle')}</h2><p class="mut">{text('technicalNote')}</p></div></div><div class="techzone"><section id="oque"><div class="wrap"><h2>{text('kitTitle')}</h2><p class="sub">{text('kitIntro')}</p><ol class="reading"><li>{text('cap1')}</li><li>{text('cap2')}</li><li>{text('cap3')}</li></ol></div></section><section id="pre"><div class="wrap"><h2>{text('requirementsTitle')}</h2><p class="reading">{text('requirementsText')}</p></div></section><section id="guia"><div class="wrap"><h2>{text('readmeFirst')}</h2>'''
 body+=step(1,'step1Title','step1Text','git clone https://github.com/inematds/ia-que-acumula.git\ncd ia-que-acumula')
 body+=step(2,'step2Title','step2Text','python3 jarvis.py novo meu-jarvis\npython3 jarvis.py pacote meu-jarvis > pedido.txt')
 body+=step(3,'step3Title','step3Text')
 body+=f'<h3>{text("expectedTitle")}</h3><pre><code>Ana | revisar proposta | sexta\nBruno | confirmar reunião | pendente</code></pre><p class="mut reading">{text("expectedNote")}</p>'
 body+=step(4,'step4Title','step4Text','python3 jarvis.py provar meu-jarvis meu-jarvis/resultado.md')
 body+=step(5,'step5Title','step5Text','python3 jarvis.py incorporar meu-jarvis /caminho/do/repo --nome ferramenta-1 --aprendizado "Guardar uma prova antes de incorporar"')
 body+=f'''</div></section><section id="testes"><div class="wrap"><h2>{text('testTitle')}</h2><p class="sub">{text('testText')}</p><pre><code>python3 -m unittest -v test_kit.py</code></pre></div></section></div><section id="fontes"><div class="wrap"><h2>{text('sourcesTitle')}</h2><p class="reading">{text('sourcesText')}</p><div class="source-links"><a href="{doc}FICHA-EXECUTIVA.md">{text('executiveFile')}</a><a href="{doc}COMECE-POR-AQUI.md">{text('startFile')}</a><a href="{doc}FONTES.md">{text('sourceFile')}</a></div></div></section></main><footer><div class="wrap"><p>{text('footer')}</p><p>{text('name')} · v1.1.0 · <a href="{REPO}">GitHub</a> · <a href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a> · <a href="https://inema.pro" target="_blank" rel="noopener">INEMA.PRO</a></p></div></footer>'''
 data=json.dumps({'agentA':t['agentA'],'agentB':t['agentB']},ensure_ascii=False)
 js='''(()=>{const theme=document.getElementById('theme'),key='ia-que-acumula-theme';function apply(light){document.body.classList.toggle('light',light);theme.textContent=light?'☾':'☀';theme.setAttribute('aria-pressed',String(light))}try{apply(localStorage.getItem(key)==='light')}catch{}theme.addEventListener('click',()=>{const light=!document.body.classList.contains('light');apply(light);try{localStorage.setItem(key,light?'light':'dark')}catch{}});const words=DATA;let alternate=false;document.getElementById('switch-agent').addEventListener('click',()=>{alternate=!alternate;document.getElementById('agent-name').textContent=alternate?words.agentB:words.agentA});document.querySelectorAll('[data-play]').forEach(button=>button.addEventListener('click',()=>{const frame=document.createElement('iframe');frame.src='https://www.youtube-nocookie.com/embed/'+button.dataset.play+'?autoplay=1';frame.title=button.getAttribute('aria-label');frame.allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';frame.allowFullscreen=true;frame.referrerPolicy='strict-origin-when-cross-origin';button.parentElement.replaceChildren(frame)}))})();'''.replace('DATA',data)
 full=f'''<!doctype html><html lang="{'pt-BR' if lang=='pt' else lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{text('name')} — {text('tagline')}</title><meta name="description" content="{text('meta')}"><link rel="canonical" href="{URL+('' if lang=='pt' else lang+'/')}">'''+''.join(f'<link rel="alternate" hreflang="{code}" href="{URL+tail}">' for code,tail in [('pt-BR',''),('en','en/'),('es','es/')])+f'''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Sora:wght@600;700;800&family=JetBrains+Mono&display=swap" rel="stylesheet"><style>{css}{extra}</style></head><body>{body}<script>{js}</script></body></html>'''
 (target/'index.html').write_text(full)
 readme=f'''# {t['name']}

**[Português](README.md) · [English](README.en.md) · [Español](README.es.md)**

[![{t['tagline']}](guia/assets/banner{suffix}.jpg)]({URL+('' if lang=='pt' else lang+'/')})

## {t['readmeWhat']}

{t['summary']}

**{t['readmeGuide']}: {URL+('' if lang=='pt' else lang+'/')}**

{t['readmeVersion']}: 1.1.0 · Python 3.10+ · MIT

## {t['readmeVideo']}

'''+''.join(f'- [{t["videoTitles"][i]}]({it["url"]})\n' for i,it in enumerate(items))+f'''
## {t['readmeFirst']}

{t['requirementsText']}

```bash
python3 jarvis.py novo meu-jarvis
python3 jarvis.py pacote meu-jarvis > pedido.txt
```

{t['step3Text']}

```text
Ana | revisar proposta | sexta
Bruno | confirmar reunião | pendente
```

{t['expectedNote']}

```bash
python3 jarvis.py provar meu-jarvis meu-jarvis/resultado.md
```

## {t['readmeScope']}

{t['step4Text']}

{t['step5Text']}

```bash
python3 jarvis.py incorporar meu-jarvis /caminho/do/repo --nome ferramenta-1 --aprendizado "Guardar uma prova antes de incorporar"
```

## {t['testTitle']}

{t['testText']}

```bash
python3 -m unittest -v test_kit.py
```

{t['graphNote']}

{t['round2Note']}
'''
 (ROOT/('README.md' if lang=='pt' else 'README.'+lang+'.md')).write_text(readme)
 print('Gerado',lang)
