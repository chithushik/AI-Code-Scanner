# 🛡️ AI Code Security & Vulnerability Scanner

An intelligent DevSecOps tool built with Python, FastAPI, and Hugging Face Transformers. This application analyzes source code snippets (Python, C++, JS) using Microsoft's **CodeBERT** model to detect security vulnerabilities such as SQL Injection, Buffer Overflow, and Cross-Site Scripting (XSS).

---

## 🌟 Features

* **AI-Powered Code Analysis**: Leverages `microsoft/codebert-base` to understand and evaluate code structure.
* **Vulnerability Detection**: Identifies critical security risks, including SQL Injections and XSS attacks.
* **Risk Scoring**: Generates a percentage-based confidence/risk score for scanned code.
* **Interactive Web UI**: A clean, user-friendly browser interface powered by FastAPI.

---

## 🛠️ Tech Stack

* **Language**: Python 3.13+
* **Framework**: FastAPI, Uvicorn
* **Machine Learning / NLP**: PyTorch, Hugging Face Transformers (`CodeBERT`)
* **Frontend**: HTML5, CSS3

---

## 🚀 Getting Started

Follow these instructions to run the project locally on your machine.

### 1. Prerequisites
Ensure you have **Python 3.10+** and **Git** installed on your system.

### 2. Clone the Repository
```bash
git clone [https://github.com/chithushik/AI-Code-Scanner.git](https://github.com/chithushik/AI-Code-Scanner.git)
cd AI-Code-Scanner