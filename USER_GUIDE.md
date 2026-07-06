# 📖 User Guide

Welcome to the **Enterprise AI Knowledge Assistant User Guide**.

This guide explains how to use every feature of the application, from uploading documents to asking intelligent questions using your private AI Knowledge Base.

---

# Table of Contents

1. Introduction
2. Application Overview
3. Administrator Dashboard
4. Uploading Documents
5. Building the Knowledge Base
6. Enterprise AI Assistant
7. Understanding Source References
8. Supported File Types
9. Best Practices
10. Troubleshooting

---

# 1. Introduction

Enterprise AI Knowledge Assistant is a private Retrieval-Augmented Generation (RAG) platform that enables organizations to transform enterprise documents into an intelligent AI-powered knowledge base.

Instead of manually searching through documents, users simply ask questions in natural language and receive accurate, source-backed answers generated from uploaded documents.

---

# 2. Application Overview

![Application Overview](docs/screenshots/home.png)

The application consists of two primary modules:

### 👤 Enterprise AI Assistant

Used by end users to ask questions about uploaded enterprise documents.

### ⚙ Administrator Dashboard

Used by administrators to upload documents, build the Knowledge Base, and monitor system statistics.

---

# 3. Administrator Dashboard

![Administrator Dashboard](docs/screenshots/admin-dashboard.png)

The Administrator Dashboard provides complete control over the Knowledge Base.

It displays:

- Total uploaded documents
- Total processed pages
- Number of chunks created
- Number of vectors generated
- Supported file types
- Knowledge Base readiness status

These metrics allow administrators to monitor document processing and verify that the AI Assistant is ready to answer questions.

---

## Upload Documents

Supported formats include:

- PDF
- DOCX
- PPTX
- XLSX
- TXT
- CSV
- PNG
- JPG
- JPEG
- EML

Click **Save Documents** after selecting one or more files.

---

## Build Knowledge Base

After uploading documents:

1. Click **Build Knowledge Base**
2. Wait for processing to complete
3. Verify the Knowledge Base status changes to **Ready**

During processing, the application automatically:

- Reads every document
- Extracts text
- Creates semantic chunks
- Generates embeddings
- Stores vectors in ChromaDB

Once complete, the AI Assistant can answer questions.

---

# 4. Enterprise AI Assistant

![Enterprise AI Assistant](docs/screenshots/chat.png)

The Enterprise AI Assistant provides a conversational interface for interacting with enterprise knowledge.

Simply type a question such as:

- What is the project health?
- Summarize the Project Charter.
- What are the highest project risks?
- Explain the deployment process.
- Which stakeholder approved this functionality?

The assistant retrieves relevant information and generates an answer using the local AI model.

---

# 5. Source References

![Source References](docs/screenshots/sources.png)

Every response includes supporting source documents.

Each source displays:

- Document name
- Document type
- Chunk ID
- Retrieved content

This allows users to verify where the answer originated.

---

# 6. Knowledge Base Workflow

The application follows the Retrieval-Augmented Generation (RAG) workflow.

```text
Upload Documents
        │
        ▼
Extract Text
        │
        ▼
Create Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Store in ChromaDB
        │
        ▼
User Question
        │
        ▼
Semantic Retrieval
        │
        ▼
Local AI (Qwen2.5)
        │
        ▼
Answer + Sources
```

---

# 7. Supported File Types

| Format | Supported |
|----------|-----------|
| PDF | ✅ |
| DOCX | ✅ |
| PPTX | ✅ |
| XLSX | ✅ |
| TXT | ✅ |
| CSV | ✅ |
| PNG | ✅ |
| JPG | ✅ |
| JPEG | ✅ |
| EML | ✅ |

---

# 8. Best Practices

For the best experience:

- Upload complete project documentation instead of isolated files.
- Rebuild the Knowledge Base after adding or updating documents.
- Use clear, natural language questions.
- Verify responses using the provided source references.
- Keep related project documents together for improved retrieval accuracy.

---

# 9. Example Questions

## Project Management

- What is the overall project health?
- What are the biggest project risks?
- Are we on track?
- Summarize the Project Charter.
- Which stakeholders approved the requirements?

---

## Human Resources

- What is the leave policy?
- Can employees work remotely?
- What benefits are available?

---

## Healthcare

- Explain the patient discharge workflow.
- What is the medication policy?

---

## Banking & Finance

- Explain the fraud detection process.
- What are the KYC requirements?

---

## Manufacturing

- What caused the previous production issue?
- Show the maintenance procedure.

---

# 10. Troubleshooting

## Knowledge Base shows "Build Required"

Upload documents and rebuild the Knowledge Base.

---

## AI cannot answer questions

Ensure:

- Documents have been uploaded.
- The Knowledge Base has been built.
- Ollama is running.
- The selected model has been downloaded.

---

## OCR does not detect text

Verify that:

- Tesseract OCR is installed.
- Image quality is sufficient.
- The image contains readable text.

---

## Slow Responses

Response time depends on:

- CPU performance
- Selected LLM
- Number of retrieved chunks
- Model size

For faster responses, use lightweight local models such as **Qwen2.5:3B**.

---

# 🎉 Congratulations

You are now ready to build and query your own private Enterprise AI Knowledge Base.

Thank you for using **Enterprise AI Knowledge Assistant**.