# IA que acumula

**[Português](README.md) · [English](README.en.md) · [Español](README.es.md)**

[![Your Jarvis evolves with you](guia/assets/banner-en.jpg)](https://inematds.github.io/ia-que-acumula/guia/en/)

## What it is

A Jarvis is a personal AI assistant that you organize for your work. IA que acumula is a study and practice kit for anyone who wants to start their own assistant or improve the agents they already use. It helps you save instructions in files, study one item in a project folder, and check a small task. That way, you can reuse your setup when you switch tools. The videos explain the idea before the technical details; the exercise uses an agent you already have.

**User guide with the six videos: https://inematds.github.io/ia-que-acumula/guia/en/**

Version: 1.1.0 · Python 3.10+ · MIT

## Videos in Portuguese

- [Are you learning AI to build or to depend on it?](https://www.youtube.com/watch?v=vB_O6xsU3l8)
- [Does your agent switch tools and forget everything? Build an evolving Jarvis](https://www.youtube.com/watch?v=h_-Hup9KPvA)
- [Can you start your own Jarvis with a simple task?](https://www.youtube.com/watch?v=dKIzL6vfJuI)
- [Will executives beg for this knowledge? My view of what comes after 2027](https://www.youtube.com/watch?v=u5r1WbLCECA)
- [Executives will ask for results: can your agent prove them?](https://www.youtube.com/watch?v=z43_SC4TXqI)
- [After 2027, who will be able to show what they can do with AI?](https://www.youtube.com/watch?v=mpg1y5G99SQ)

## First use

To run the kit, use Python 3.10 or later and a terminal. For the AI portion, use an agent you already have access to. The commands below use python3, which is common on Linux and macOS; on Windows, replace that beginning with py -3. The kit program does not require an API key.

```bash
python3 jarvis.py novo meu-jarvis
python3 jarvis.py pacote meu-jarvis > pedido.txt
```

Open the meu-jarvis folder in your agent, or copy the contents of pedido.txt into the chat you already use. Ask: read AGENTS.md and TAREFA.md, organize the tasks, and save the result in resultado.md. If you’re using a chat on its own, copy the response into a file named resultado.md inside the meu-jarvis folder. Then check the two lines against the source.

```text
Ana | revisar proposta | sexta
Bruno | confirmar reunião | pendente
```

The names, tasks, and values sexta and pendente are literal values from the exercise and remain in Portuguese in all three languages.

```bash
python3 jarvis.py provar meu-jarvis meu-jarvis/resultado.md
```

## Checker scope

Run the checker after saving the response in resultado.md. It needs to find Ana, Bruno, sexta associated with Ana, and pendente associated with Bruno. Exit code 0 means it found these markers; this is not a general validation of any AI response.

Use a repository already on your machine. Replace /caminho/do/repo with the actual path. The record waits for review; ask the agent to explain the requirements, license, and a small change before installing or running anything.

```bash
python3 jarvis.py incorporar meu-jarvis /caminho/do/repo --nome ferramenta-1 --aprendizado "Guardar uma prova antes de incorporar"
```

## Checking the kit itself

The seven tests check file preservation, context package, incorporation without execution, safe names, a repository without a README, a symbolic link, and the positive/negative example. The published package was also extracted and run in a clean folder.

```bash
python3 -m unittest -v test_kit.py
```

The exponential curve is a conceptual illustration in Portuguese, with no numerical scale, dates, or measured forecast. It represents the idea of acceleration; it does not show that every AI capability grows this way.

The competition for professionals after 2027 is Nei’s view of a possible scenario, with no guarantee of employment or income.
