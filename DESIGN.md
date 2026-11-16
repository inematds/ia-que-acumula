---
name: IA que acumula
description: Sistema visual existente do guia INEMA dark/âmbar com tema claro.
colors:
  amber: "#E2A23B"
  amber-soft: "#f0c070"
  club: "#38bdf8"
  pro: "#cbd5e1"
  background: "#0c0c10"
  background-raised: "#14141b"
  card: "#16161e"
  line: "#272730"
  text: "#e9e9ee"
  muted: "#9a9aa6"
  light-amber: "#b9791d"
  light-amber-soft: "#a16207"
  light-club: "#0369a1"
  light-pro: "#b45309"
  light-background: "#f6f7f9"
  light-background-raised: "#eceef2"
  light-card: "#ffffff"
  light-line: "#e1e3ea"
  light-text: "#1a1a22"
  light-muted: "#5b5b68"
typography:
  display:
    fontFamily: "Sora, sans-serif"
    fontSize: "clamp(2.2rem, 5vw, 3.5rem)"
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-.025em"
  headline:
    fontFamily: "Sora, sans-serif"
    fontSize: "clamp(1.5rem, 3.4vw, 2.1rem)"
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-.02em"
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "16px"
    lineHeight: 1.65
  label:
    fontFamily: "Sora, sans-serif"
    fontSize: ".72rem"
    fontWeight: 600
    letterSpacing: ".14em"
  code:
    fontFamily: '"JetBrains Mono", monospace'
    fontSize: ".86rem"
    lineHeight: 1.6
rounded:
  language: "6px"
  control: "10px"
  player: "12px"
  card: "14px"
  hero: "16px"
spacing:
  grid: "16px"
  card: "20px"
  gutter: "22px"
  section: "62px"
components:
  button-primary:
    backgroundColor: "{colors.amber}"
    textColor: "#1a1206"
    rounded: "{rounded.control}"
    padding: ".6em 1.05em"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    rounded: "{rounded.control}"
    padding: ".6em 1.05em"
  card:
    backgroundColor: "{colors.card}"
    rounded: "{rounded.card}"
    padding: "{spacing.card}"
---

# Design System: IA que acumula

## Overview

**Creative North Star: "Guia INEMA dark/âmbar"**

Documentação do sistema já implementado, preservando o template projetos-landing-guia fixado pelo usuário. Superfícies escuras, títulos geométricos e acentos âmbar organizam textos, imagens explicativas e exercícios; o tema claro mantém os mesmos papéis visuais. A expressão acima descreve o template existente, sem propor uma nova identidade.

**Key Characteristics:**

- Hierarquia tipográfica Sora/Inter, com monoespaçada nos comandos.
- Painéis com borda fina, cantos arredondados e imagens grandes.
- Identidade INEMA.CLUB/PRO e navegação PT/EN/ES persistentes.

Fontes: `guia/index.html`, `scripts/template-base.css` e `PRODUCT.md`; capturas existentes em `../output/ia-que-acumula/qa-guia/`. Esta documentação registra código e evidência visual existentes, sem alterar a interface.

## Colors

### Primary

Âmbar destaca nome do projeto, título principal, ações, passos e links. O âmbar suave serve ao realce de código no template.

### Secondary

Ciano identifica INEMA.CLUB e o contorno de foco. PRO usa cinza prateado no escuro e âmbar profundo no claro.

### Neutral

O fundo quase preto recebe superfícies discretamente mais claras; texto claro e cinza secundário mantêm a hierarquia. O tema claro troca esses papéis por fundos frios claros, cartões brancos e texto escuro. Os tokens `light-*` correspondem às substituições de `body.light`, não a uma segunda composição.

## Typography

**Display Font:** Sora, sans-serif. **Body Font:** Inter, system-ui, sans-serif. **Label/Mono Font:** Sora para rótulos; JetBrains Mono, monospace para comandos. As fontes são carregadas pelo Google Fonts.

Títulos têm peso forte, entrelinha curta e espaçamento negativo; o corpo mantém entrelinha aberta. O título principal passa a (2.2rem) até (600px). Títulos de cartões usam (1.05rem); títulos de vídeos usam (1.04rem) com entrelinha (1.4). Subtítulos têm largura máxima de (62ch), trechos de leitura (74ch) e apresentação inicial (34ch). Rótulos de seção usam caixa alta; comandos preservam sua grafia literal.

## Layout

Container central com máximo de (1160px), incluindo margens internas laterais de (22px). Hero em duas colunas (1.1fr/.9fr), intervalo de (40px), padding vertical de (74px); até (780px), uma coluna e padding vertical de (48px). Seções usam padding vertical do token `section`, reduzido a (42px) até (600px).

Grade de cartões em três colunas, duas até (820px), uma até (540px). Vídeos usam três colunas, duas até (940px), uma até (600px), com intervalos de (28px) na vertical e (20px) na horizontal. Passos técnicos reservam (46px) à numeração e usam coluna de conteúdo com `minmax(0,1fr)`. Código longo rola horizontalmente.

## Elevation & Depth

Predominam camadas tonais e bordas de (1px). A figura do hero usa sombra (`0 30px 80px -30px #000`); o controle de reprodução tem drop-shadow (`0 3px 9px #0009`). A navegação escura combina fundo translúcido com blur de (12px); no claro, recebe fundo opaco. O template define brilho radial âmbar no hero, mas a página atual não instancia esse elemento.

## Shapes

Controles, players, cartões e imagem do hero usam os raios correspondentes do frontmatter. O botão de tema é quadrado arredondado (38px), reduzido a (34px) até (520px). Passos são quadrados arredondados (46px). A reprodução usa círculo central (56px) com triângulo âmbar. Evitar transformar cartões de vídeo em painéis: sua moldura envolve apenas a imagem/player.

## Components

### Buttons

Primário preenchido em âmbar, texto escuro, Sora (600); secundário transparente com borda e texto normal. Não há transição nem transformação de hover nesses botões. Links e botões recebem foco visível com contorno ciano (3px), afastado (4px). O botão de tema muda a borda para âmbar no hover.

### Cards / Containers

Cartões de conteúdo têm fundo próprio, borda fina, raio `card` e padding `card`. A simulação usa fundo elevado e padding (26px), reduzido a (18px) até (600px). O início técnico separa a leitura com fundo elevado e borda superior âmbar (2px). Blocos de código permanecem escuros também no tema claro.

### Navigation

Barra sticky no topo, altura de (60px), links de seção secundários, marca com SVG de camadas, INEMA.CLUB/PRO, idiomas, tema e acesso ao GitHub. Até (760px), links de seção somem; até (520px), a barra quebra em duas linhas, com controles distribuídos na segunda. O idioma atual recebe fundo âmbar translúcido e `aria-current`; são links entre páginas, sem tradução dinâmica.

### Tema

Alterna a classe `light`, os símbolos sol/lua e `aria-pressed`. A preferência fica em `localStorage` na chave `ia-que-acumula-theme`; falhas de armazenamento são toleradas. Escuro é o padrão sem preferência salva.

### Vídeos sob demanda

Seis cartões, em duas rodadas de três, exibem miniatura local 16:9, botão de reprodução com nome acessível, título, canal e idioma. O iframe `youtube-nocookie.com` é criado somente no clique e substitui o botão; cada cartão mantém link externo para assistir no YouTube. Áudio e legendas são em português também nas páginas EN/ES.

### Simulação visual

“Trocar agente” alterna somente o texto Agente A/Agente B em um elemento `role="status"`; o contexto visual permanece. O aviso explica que a demonstração não executa IA. Não existem campos de entrada, chat ou integração de modelo nessa interface.

### Leitura e acesso

O guia favorece compreensão, com resumo, vídeos e explicação antes da área técnica. O link de salto aparece ao receber foco. Âncoras têm margem de rolagem (100px). `prefers-reduced-motion` desliga rolagem suave, animações e transições.

## Do's and Don'ts

### Do:

- **Do** preservar o template INEMA dark/âmbar e seu tema claro equivalente.
- **Do** manter INEMA.CLUB/PRO, seletor PT/EN/ES e controles acessíveis.
- **Do** preservar proporção das imagens, limites de leitura e comandos literais.

### Don't:

- **Don't** substituir os players sob demanda por iframes carregados na abertura.
- **Don't** apresentar a simulação como execução real de IA.
- **Don't** apresentar a curva conceitual como gráfico de dados medidos.
