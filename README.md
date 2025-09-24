# 🤖 AI Code Review Bot

An interactive **Streamlit web app** powered by **Ollama Cloud** that reviews your code files and generates a structured report.  
The app highlights **bugs, style issues, performance bottlenecks, and security concerns** — all presented in a neat **dark-themed HTML report** that you can view in the browser or download.  

---

## ✨ Features

- 📂 Upload a single code file (`.py`, `.js`, `.java`, `.cpp`, `.ts`, `.go`).  
- 🔍 AI-powered review using large **cloud-hosted coding models** (e.g. `qwen3-coder:480b-cloud`).  
- 📝 Structured feedback report with sections:
  - Bugs & Errors  
  - Style & Formatting  
  - Performance Issues  
  - Security Concerns  
  - Suggestions & Improvements  
- 🌙 Dark-themed HTML output (in-app and downloadable).  
- 🚀 Runs locally, no GPU required (thanks to Ollama Cloud).  

---

## 📦 Installation

### 1. Clone this repo
```bash
git clone https://github.com/nilay220303/ai-code-review-bot.git
cd ai-code-review-bot
```

### 2. Install dependencies
Make sure you have Python 3.9+ installed.
```bash
pip install -r requirements.txt
```
Minimal Dependencies:
```nginx
streamlit
markdown
ollama
```

### Get Ollama API Key
- Login to Ollama Cloud
- Go to Settings and generate API Key
- Store it safely

---

## 🚀 Usage
Run the Streamlit App:
```bash
streamlit run code_review_app.py
```
---

## 🖥️ App Demo

1. Enter Ollama API Key.
2. Upload a code file (Python, JavaScript, etc.).
2. Click **Run Code Review**.
3. Instantly see a **HTML report**.
4. Optionally, **download the review as a `.html` file**.
