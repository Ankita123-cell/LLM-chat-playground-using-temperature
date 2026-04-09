# LLM Chat Playground

A Python-based interactive playground to explore how *temperature settings affect LLM outputs* across different use cases.

## Overview

This project helps compare how large language model responses change based on *temperature, using both **manual controls* and *task-based defaults*.

It is designed as a small experimentation tool for understanding:
- response creativity
- determinism vs variation
- prompt behavior across different settings

---

## Features

- *Temperature dropdown*
  - Choose from 3 predefined temperature settings

- *Task-based default values*
  - Pre-configured temperatures based on task type (e.g. factual vs creative)

- *Temperature slider*
  - Fine-tune model behavior interactively

- *3-way comparison mode*
  - Compare outputs across 3 different temperature values side by side

- *Quote-rich output display*
  - Better readability and output presentation

---

## Why I built this

A single parameter like *temperature* can significantly change how an LLM responds.

This project was built to better understand:
- when low temperature works better
- when higher temperature improves output
- how model “personality” shifts across tasks

---

## Tech Stack

- Python
- Streamlit
- ChatGpt chat model

---

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd <your-project-folder>

Create a .env file and add your API key
OPENAI_API_KEY=your_api_key_here

Bash
python main.py
