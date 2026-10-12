# 📚 Multi-Agent AI Study Assistant

A personalized learning platform powered by multiple AI agents for study planning, quiz generation, tutoring, and RAG-based document Q&A.

## 🚀 Live Demo

The app is live here:

https://study-assistant-jyv1.onrender.com

## 🌟 What this app does

- Create a personalized learning plan based on the student's goals, time, and level
- Generate study roadmaps and milestones
- Recommend relevant learning resources
- Generate quizzes and explanations
- Act as an AI tutor for follow-up questions
- Answer questions from uploaded documents using RAG

## 🏗️ Tech Stack

- Python 3.12
- Streamlit
- LangChain
- ChromaDB
- OpenAI
- Groq
- Phidata

## 🔐 Required environment variables

Create a `.env` file in the project root with:

```bash
GROQ_API_KEY=your_groq_key_here
OPENAI_API_KEY=your_openai_key_here
```

You can copy from the example file:

```bash
cp .env.example .env
```

## 🧪 Local setup

### 1) Create and activate a virtual environment

```bash
cd /Users/indranil/Downloads/study-assistant
python3.12 -m venv .venv312
source .venv312/bin/activate
```

### 2) Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3) Run the app locally

```bash
streamlit run app.py
```

Or with the venv Python explicitly:

```bash
.venv312/bin/python -m streamlit run app.py
```

## ☁️ Render deployment

The project is already configured for Render deployment.

### Required files

Create `runtime.txt` in the project root:

```text
python-3.12.13
```

### Render settings

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port $PORT
```

Environment variables:

- `GROQ_API_KEY`
- `OPENAI_API_KEY`

## 📦 Push to GitHub

If the repository already exists, use:

```bash
git add .
git commit -m "Initial commit"
git push -u origin main
```

If the remote is not set yet, run:

```bash
git remote set-url origin https://github.com/rohanbhati0912/study-assistant.git
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main
```

## 🧭 Project structure

```text
study-assistant/
├── app.py
├── agent_handler.py
├── config.py
├── prompts.yaml
├── rag_helper.py
├── study_agents.py
├── requirements.txt
├── .env.example
├── runtime.txt
├── README.md
└── .streamlit/
```

## 🛠️ Troubleshooting

### Python version issue

This app is validated on Python 3.12. Do not use Python 3.14 for deployment.

### Streamlit command missing

```bash
python3.12 -m streamlit run app.py
```

### Missing API key errors

Make sure `.env` is present and contains valid keys.

### Dependency issues

```bash
pip install -r requirements.txt
```

## 📌 Notes

- Use Python 3.12 for local and deployment environments.
- Keep your API keys in environment variables or `.env`, not hardcoded in source files.
- The live demo URL is the Render deployment at https://study-assistant-jyv1.onrender.com

## 👤 Author

Rohan Bhati
