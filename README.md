## 🧠 Project Overview: What We Built

**Smart Meeting Summarizer** is an end-to-end AI-powered tool that transforms raw meeting recordings into structured insights — in just a few clicks.

### 🎯 What It Does

1. **Transcribes meeting audio/video** using [OpenAI Whisper](https://openai.com/research/whisper)
2. **Summarizes the conversation** using GPT-4 with a custom prompt
3. **Extracts action items** clearly and concisely
4. Provides a **simple Streamlit interface** for non-technical users
5. Keeps API keys secure via `.env` loading

---

### 🧱 How It Works (Architecture)

- **Frontend/UI**: Built with [Streamlit](https://streamlit.io/)
  - Upload an `.mp3`, `.wav`, `.m4a`, or `.mp4` file
  - Displays transcript, summary, and action items

- **Transcription**: Powered by OpenAI's Whisper model (`tiny`/`base`)
  - Converts speech to text locally

- **Summarization + Actions**:
  - Uses GPT-4 via OpenAI API
  - Custom system prompt guides GPT to:
    - Provide a structured meeting summary
    - Output a clean bullet-point list of action items

- **Environment Management**:
  - Project uses a virtual environment (`venv`)
  - API key is securely loaded from a `.env` file using `python-dotenv`

---

### 💡 Why It’s Cool

- ⚡ **Instant productivity** boost: no more manual note-taking
- 📎 AI-native solution that integrates two powerful models
- 🧪 Easy to demo & extend: plug in calendar APIs, topic tagging, etc.
- 🧠 Great showcase of applied NLP, multimodal AI, and Python engineering

---

### 📌 Technologies Used

| Tool           | Role                            |
|----------------|---------------------------------|
| Python         | Core language                   |
| Streamlit      | Web interface                   |
| OpenAI Whisper | Audio transcription             |
| GPT-4          | Summarization + task extraction |
| dotenv         | Secure API key management       |
| ffmpeg         | Audio processing backend        |
