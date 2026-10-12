# Study Assistant

A multi-agent AI study app that helps students plan learning, generate personalized quizzes, create roadmaps, and get tutoring support with uploaded documents.

## Live demo

https://study-assistant-jyv1.onrender.com

## About

Study Assistant is an AI-powered study companion built to help students learn faster, stay organized, and study with more confidence. It combines multiple specialized agents for student analysis, learning-path planning, quiz generation, tutoring, and document-based Q&A, giving users a complete digital study experience in one place.

This project is designed for students, learners, and academic users who want a more personalized and structured way to revise concepts, prepare for exams, and work through course materials. It brings together AI guidance, smart recommendations, and interactive learning tools in a simple Streamlit interface.

The app is currently live and ready to use at the Render demo link above, making it easy to explore the assistant without setting up a local environment first.

## Overview

Study Assistant is a Streamlit-based learning platform built around multiple specialized AI agents. It helps students:

- analyze their current knowledge level
- define goals and study constraints
- generate personalized learning roadmaps
- find relevant learning resources
- create quizzes and explanations
- ask follow-up questions through an AI tutor
- search and answer questions from uploaded study material using RAG

## Features

- Personalized student analysis
- Learning roadmap generation
- Smart resource recommendations
- Adaptive quiz generation
- AI tutoring experience
- Document Q&A with uploaded PDFs and notes
- Multi-provider AI support with Groq and OpenAI

## Tech stack

- Python 3.12
- Streamlit
- LangChain
- ChromaDB
- Phidata
- Groq
- OpenAI

## Project structure

```text
study-assistant/
├── app.py
├── agent_handler.py
├── config.py
├── prompts.yaml
├── rag_helper.py
├── study_agents.py
├── requirements.txt
├── runtime.txt
├── .env.example
├── README.md
├── .streamlit/
└── .venv312/
```

## Setup

### 1) Clone the repository

```bash
git clone https://github.com/rohanbhati0912/study-assistant.git
cd study-assistant
```

### 2) Create a virtual environment

```bash
python3.12 -m venv .venv312
source .venv312/bin/activate
```

### 3) Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4) Add environment variables

Create a `.env` file in the root folder:

```bash
GROQ_API_KEY=your_groq_key
OPENAI_API_KEY=your_openai_key
```

You can also copy the example file:

```bash
cp .env.example .env
```

## Run locally

```bash
streamlit run app.py
```

If needed, run with the venv Python directly:

```bash
.venv312/bin/python -m streamlit run app.py
```

## Render deployment

This project is set up for Render.

### Create runtime.txt

```text
python-3.12.13
```

### Render build settings

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port $PORT
```

Environment variables to add in Render:

- `GROQ_API_KEY`
- `OPENAI_API_KEY`

## GitHub push

If the repo already exists:

```bash
git add .
git commit -m "Initial commit"
git push -u origin main
```

If the remote is not set:

```bash
git remote set-url origin https://github.com/rohanbhati0912/study-assistant.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

## Troubleshooting

### Python version error

Use Python 3.12. Do not use Python 3.14 for this project.

### Missing API keys

Ensure your `.env` file exists and contains valid keys.

### Streamlit not found

```bash
python3.12 -m streamlit run app.py
```

### Dependency issues

```bash
pip install -r requirements.txt
```

## Notes

- The deployment is live on Render.
- Keep API keys in environment variables instead of hardcoding them.
- The app is designed for educational and study-use scenarios.

## Running tests

Activate your virtual environment, then install the project and test dependencies:

```bash
python -m pip install -e .
python -m pip install pytest
```

Run the test suite:

```bash
python -m pytest -q
```

Tests should run without real AI API credentials. GitHub Actions runs the same test command on pushes and pull requests.

## Author

Rohan Bhati
