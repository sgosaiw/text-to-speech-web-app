# 🗣️ Text-to-Speech Web App

A powerful and simple web-based Text-to-Speech (TTS) generator built using [Streamlit](https://streamlit.io/) and [Edge-TTS](https://github.com/rany2/edge-tts).

## ✨ Features
*   **Neural Voices**: Choose from high-quality male and female voices (English US/UK).
*   **Customization**: Adjust **Speed** and **Pitch** to fine-tune the output.
*   **Previews**: Listen to the generated audio directly in your browser.
*   **Download**: Export as `MP3` or `WAV` for offline use.
*   **Privacy**: No API keys required; runs locally on your machine.

## 🚀 Quick Start
1.  **Run the App**:
    ```bash
    streamlit run text_to_speech_app.py
    ```
2.  **Usage**:
    *   Open the URL shown in the terminal (usually `http://localhost:8501`).
    *   Paste your text into the text area.
    *   Select your preferred voice and settings from the Sidebar.
    *   Click **Generate Speech**.

## ⚠️ Known Issues
*   **Playback Cutoff**: On some browsers, the very first time you play an audio file, the first few milliseconds might be silent or "cut off" due to browser buffering.
    *   *Workaround*: Simply replay the audio (click pause/play again), and the full sentence will be heard.

## 📦 Requirements
*   Python 3.8+
*   See `requirements.txt` for dependencies.

