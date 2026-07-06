# 🚀 Installation Guide

Welcome to **Enterprise AI Knowledge Assistant**.

This guide will walk you through setting up the application on your local machine from scratch.

---

# 📋 Prerequisites

Before getting started, ensure the following software is installed.

| Software | Version |
|-----------|----------|
| Python | 3.11 or later |
| Git | Latest |
| Ollama | Latest |
| Tesseract OCR | Latest |
| Windows 10/11, macOS, or Linux | Supported |

---

# 💻 Step 1 – Clone the Repository

Open a terminal or Command Prompt and clone the repository.

```bash
git clone https://github.com/MautikPatel/Enterprise-AI-Knowledge-Assistant.git
```

Navigate into the project folder.

```bash
cd Enterprise-AI-Knowledge-Assistant
```

---

# 🐍 Step 2 – Create a Python Virtual Environment

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

If activated successfully, your terminal should display:

```text
(.venv)
```

---

# 📦 Step 3 – Install Python Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

Depending on your internet connection, this may take several minutes.

---

# 🤖 Step 4 – Install Ollama

Download and install Ollama.

👉 https://ollama.com/download

After installation, verify that Ollama is available.

```bash
ollama --version
```

---

# 🧠 Step 5 – Download the AI Model

Pull the default Large Language Model used by this project.

```bash
ollama pull qwen2.5:3b
```

This downloads approximately 2 GB of model data.

To verify the installation:

```bash
ollama list
```

Expected output:

```text
NAME
qwen2.5:3b
```

---

# 🔍 Step 6 – Install Tesseract OCR

Tesseract is required for extracting text from image-based documents.

### Windows

Download and install:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, add the installation directory to your system PATH.

Example:

```text
C:\Program Files\Tesseract-OCR
```

Verify the installation.

```bash
tesseract --version
```

---

# ▶️ Step 7 – Start Ollama

Open a terminal and run:

```bash
ollama serve
```

Keep this terminal open while using the application.

> **Note:** On many systems, Ollama runs as a background service automatically. If that's the case, you can skip this step.

---

# 🚀 Step 8 – Launch the Application

Open a new terminal.

Ensure the virtual environment is activated.

Run:

```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

If it doesn't, navigate to:

```text
http://localhost:8501
```

---

# 📂 Step 9 – Upload Enterprise Documents

1. Open the **Administrator Dashboard**.
2. Upload one or more supported documents.
3. Click **Build Knowledge Base**.
4. Wait until the Knowledge Base status changes to **Ready**.

The system is now prepared to answer questions.

---

# 💬 Step 10 – Start Asking Questions

Switch to the **Enterprise AI Assistant**.

Example questions:

- What is the overall project health?
- What are the highest project risks?
- Summarize the project charter.
- Who approved this functionality?
- Explain the deployment process.
- What is the company leave policy?
- Summarize the fraud detection rules.

The assistant retrieves the most relevant document content and generates an answer using the local AI model.

---

# 📁 Supported Document Types

- PDF
- DOCX
- PPTX
- XLSX
- TXT
- CSV
- EML
- PNG
- JPG
- JPEG

---

# 🔒 Privacy

Enterprise AI Knowledge Assistant runs entirely on your local machine.

- No cloud AI services
- No external API calls
- No document uploads to third-party providers
- Your enterprise data remains private

---

# 🛠 Troubleshooting

## Python Not Found

Verify Python is installed.

```bash
python --version
```

If Python is not recognized, reinstall Python and ensure **Add Python to PATH** is selected during installation.

---

## Ollama Not Found

Verify the installation.

```bash
ollama --version
```

If the command is not recognized, reinstall Ollama or add it to your system PATH.

---

## Tesseract Not Found

Verify:

```bash
tesseract --version
```

If unavailable, ensure the installation directory has been added to your PATH.

---

## Model Not Found

Download the model again.

```bash
ollama pull qwen2.5:3b
```

---

## Application Does Not Start

Ensure the virtual environment is activated.

Reinstall dependencies if necessary.

```bash
pip install -r requirements.txt
```

---

## Knowledge Base Status Shows "Build Required"

Open the **Administrator Dashboard** and click **Build Knowledge Base** after uploading documents.

---

# 🎉 You're Ready!

Congratulations! 🎉

Your local Enterprise AI Knowledge Assistant is now ready to transform enterprise documents into an intelligent, searchable knowledge base powered entirely by local AI.

Happy exploring! 🚀