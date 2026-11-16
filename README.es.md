# IA que acumula

**[Português](README.md) · [English](README.en.md) · [Español](README.es.md)**

[![Tu Jarvis evoluciona contigo](guia/assets/banner-es.jpg)](https://inematds.github.io/ia-que-acumula/guia/es/)

## Qué es

Un Jarvis es un asistente personal de IA que organizas para tu trabajo. IA que acumula es un kit de estudio y práctica para quienes quieren empezar su propio asistente o mejorar los agentes que ya usan. Ayuda a guardar instrucciones en archivos, estudiar una parte de la carpeta de un proyecto y revisar una tarea pequeña. Así, puedes reutilizar tu base cuando cambies de herramienta. Los videos explican la idea antes de la parte técnica; el ejercicio usa un agente que ya tengas.

**Guía de uso con los seis vídeos: https://inematds.github.io/ia-que-acumula/guia/es/**

Versión: 1.1.0 · Python 3.10+ · MIT

## Vídeos en portugués

- [¿Estás aprendiendo IA para construir o para depender de ella?](https://www.youtube.com/watch?v=vB_O6xsU3l8)
- [¿Tu agente cambia de herramienta y lo olvida todo? Construye un Jarvis que evoluciona](https://www.youtube.com/watch?v=h_-Hup9KPvA)
- [¿Puedes empezar tu propio Jarvis con una tarea sencilla?](https://www.youtube.com/watch?v=dKIzL6vfJuI)
- [¿Los ejecutivos suplicarán por este conocimiento? Mi visión para después de 2027](https://www.youtube.com/watch?v=u5r1WbLCECA)
- [El ejecutivo pedirá resultados: ¿puede tu agente demostrarlos?](https://www.youtube.com/watch?v=z43_SC4TXqI)
- [Después de 2027, ¿quién podrá mostrar lo que sabe hacer con IA?](https://www.youtube.com/watch?v=mpg1y5G99SQ)

## Primer uso

Para ejecutar el kit, usa Python 3.10 o posterior y un terminal. Para la parte de IA, usa un agente al que ya tengas acceso. Los comandos siguientes usan python3, habitual en Linux y macOS; en Windows, sustituye ese inicio por py -3. El programa del kit no necesita ninguna clave de API.

```bash
python3 jarvis.py novo meu-jarvis
python3 jarvis.py pacote meu-jarvis > pedido.txt
```

Abre la carpeta meu-jarvis en tu agente, o copia el contenido de pedido.txt en el chat que ya usas. Pide: lee AGENTS.md y TAREFA.md, organiza las tareas y guarda resultado.md. Si solo estás usando un chat, copia la respuesta en un archivo llamado resultado.md dentro de la carpeta meu-jarvis. Después, revisa las dos líneas junto con la fuente.

```text
Ana | revisar proposta | sexta
Bruno | confirmar reunião | pendente
```

Los nombres, las tareas y los valores sexta y pendente son literales del ejercicio y permanecen en portugués en los tres idiomas.

```bash
python3 jarvis.py provar meu-jarvis meu-jarvis/resultado.md
```

## Alcance del verificador

Ejecuta el verificador después de guardar la respuesta en resultado.md. Debe encontrar Ana, Bruno, sexta asociado con Ana y pendente asociado con Bruno. El código de salida 0 indica que encontró esas marcas; no es una validación general de cualquier respuesta de IA.

Usa un repositorio que ya esté en tu máquina. Sustituye /caminho/do/repo por la ruta real. El registro queda pendiente de revisión; pide al agente que explique los requisitos, la licencia y un pequeño cambio antes de instalar o ejecutar nada.

```bash
python3 jarvis.py incorporar meu-jarvis /caminho/do/repo --nome ferramenta-1 --aprendizado "Guardar uma prova antes de incorporar"
```

## Comprobación del propio kit

Las siete pruebas verifican la conservación de archivos, el paquete de contexto, la incorporación sin ejecución, los nombres seguros, un repositorio sin README, un enlace simbólico y el ejemplo positivo/negativo. El paquete publicado también se descomprimió y ejecutó en una carpeta limpia.

```bash
python3 -m unittest -v test_kit.py
```

La curva exponencial es una ilustración conceptual en portugués, sin escala numérica, fechas ni predicción medida. Representa la idea de aceleración; no demuestra que todas las capacidades de IA crezcan así.

La competencia por profesionales después de 2027 es la visión de Nei sobre un escenario posible, sin garantía de empleo ni ingresos.
