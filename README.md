# 📄 PDF Summarizer (Local AI Powered)

A production-ready PDF summarization tool using **FastAPI + Ollama (Local LLMs)**.

## 🚀 Features

- 📂 Upload PDF files
- 🧠 AI-powered summarization (local models)
- 🎯 Multiple summary modes:
  - Brief
  - Detailed
  - Bullet Points
  - Executive Summary
- ⚡ Fast processing using chunking
- 🔒 Runs fully offline (privacy-friendly)

## 🛠 Tech Stack

- Backend: FastAPI
- AI: Ollama (TinyLlama / Mistral)
- PDF Processing: pypdf
- Environment: Python (venv)

## 📁 Project Structure
backend/
├── app/
│ ├── routes/
│ ├── services/
│ ├── core/
│ └── main.py
├── requirements.txt


## ⚙️ Setup Instructions

### 1. Clone repo

```bash
git clone https://github.com/divyamk521/pdf_summarizer.git
cd pdf-summarizer/backend


### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt

4. Run server
uvicorn app.main:app --reload
5. Open API Docs
http://127.0.0.1:8000/docs
🤖 Run Ollama
ollama pull tinyllama
ollama serve

📌 Future Improvements
Streaming responses
Multi-chunk optimization
Frontend UI (React)
Export summaries
👨‍💻 Author

Divya M K
