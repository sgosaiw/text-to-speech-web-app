# 💿 Installation Guide

Follow these steps to set up the Text-to-Speech Web App on a new computer.

## Prerequisites
*   **Python**: Ensure Python 3.8 or newer is installed.
    *   [Download Python](https://www.python.org/downloads/)
*   **Git** (Optional): To clone the repository.

## Installation Steps

### 1. Get the Code
Download the code directory or clone the repository:
```bash
git clone <repository-url>
cd text-to-speech-web-app
```

### 2. Create a Virtual Environment (Recommended)
It's best practice to run Python apps in an isolated environment.

**Windows**:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Mac/Linux**:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
Install the required packages (`streamlit`, `edge-tts`):
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Streamlit server:
```bash
streamlit run text_to_speech_app.py
```
A browser window should automatically open at `http://localhost:8501`.

---

## ☁️ Running on Google Colab (Cloud)
You can run this app entirely in the cloud using Google Colab!

1.  Open the `run_on_colab.ipynb` notebook (if providing checking it into repo) OR create a new Colab notebook.
2.  Run the installation and tunnel cells (see `run_on_colab.ipynb` for code).
3.  Click the public URL provided by `localtunnel` / `ngrok`.
