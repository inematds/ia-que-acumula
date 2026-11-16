# IA que acumula

**[Português](README.md) · [English](README.en.md) · [Español](README.es.md)**

[![Seu Jarvis evolui com você](guia/assets/banner.jpg)](https://inematds.github.io/ia-que-acumula/guia/)

## O que é

Um Jarvis é um assistente pessoal de IA que você organiza para o seu trabalho. IA que acumula é um kit de estudo e prática para quem quer começar o próprio assistente ou melhorar os agentes que já usa. Ele ajuda a guardar instruções em arquivos, estudar uma peça da pasta de um projeto e conferir uma tarefa pequena. Assim, você pode reaproveitar sua base quando trocar de ferramenta. Os vídeos explicam a ideia antes da parte técnica; o exercício usa um agente que você já tenha.

**Guia de uso com os seis vídeos: https://inematds.github.io/ia-que-acumula/guia/**

Versão: 1.1.0 · Python 3.10+ · MIT

## Vídeos em português

- [Você está aprendendo IA para construir ou para depender?](https://www.youtube.com/watch?v=vB_O6xsU3l8)
- [Seu agente muda de ferramenta e esquece tudo? Construa um Jarvis que evolui](https://www.youtube.com/watch?v=h_-Hup9KPvA)
- [Você consegue começar seu próprio Jarvis com uma tarefa simples](https://www.youtube.com/watch?v=dKIzL6vfJuI)
- [Executivos vão suplicar por este conhecimento? Minha visão para depois de 2027](https://www.youtube.com/watch?v=u5r1WbLCECA)
- [O executivo vai pedir resultado: seu agente consegue provar?](https://www.youtube.com/watch?v=z43_SC4TXqI)
- [Depois de 2027, quem vai conseguir mostrar o que sabe fazer com IA?](https://www.youtube.com/watch?v=mpg1y5G99SQ)

## Primeiro uso

Para executar o kit, use Python 3.10 ou mais recente e um terminal. Para a parte de IA, use um agente ao qual você já tenha acesso. Os comandos abaixo usam python3, comum em Linux e macOS; no Windows, substitua esse início por py -3. Nenhuma chave de API é necessária ao programa do kit.

```bash
python3 jarvis.py novo meu-jarvis
python3 jarvis.py pacote meu-jarvis > pedido.txt
```

Abra a pasta meu-jarvis no seu agente, ou copie o conteúdo de pedido.txt para o chat que você já usa. Peça: leia AGENTS.md e TAREFA.md, organize as tarefas e grave resultado.md. Se estiver usando só um chat, copie a resposta para um arquivo chamado resultado.md dentro da pasta meu-jarvis. Depois, confira as duas linhas com a fonte.

```text
Ana | revisar proposta | sexta
Bruno | confirmar reunião | pendente
```

Os nomes, tarefas e os valores sexta e pendente são literais do exercício e permanecem em português nos três idiomas.

```bash
python3 jarvis.py provar meu-jarvis meu-jarvis/resultado.md
```

## Escopo do conferidor

Rode o conferidor depois de salvar a resposta em resultado.md. Ele precisa encontrar Ana, Bruno, sexta associada a Ana e pendente associado a Bruno. Código de saída 0 indica que encontrou essas marcas; não é uma validação geral de qualquer resposta de IA.

Use um repositório que já esteja na sua máquina. Troque /caminho/do/repo pelo caminho real. O registro fica aguardando revisão; peça ao agente que explique requisitos, licença e uma mudança pequena antes de instalar ou executar algo.

```bash
python3 jarvis.py incorporar meu-jarvis /caminho/do/repo --nome ferramenta-1 --aprendizado "Guardar uma prova antes de incorporar"
```

## Conferência do próprio kit

Os sete testes verificam preservação de arquivos, pacote de contexto, incorporação sem execução, nomes seguros, repositório sem README, link simbólico e o exemplo positivo/negativo. O pacote publicado também foi extraído e executado em uma pasta limpa.

```bash
python3 -m unittest -v test_kit.py
```

A curva exponencial é uma ilustração conceitual em português, sem escala numérica, datas ou previsão medida. Ela representa a ideia de aceleração; não demonstra que toda capacidade de IA cresce assim.

A disputa por profissionais depois de 2027 é a visão do Nei sobre um cenário possível, sem garantia de emprego ou renda.
