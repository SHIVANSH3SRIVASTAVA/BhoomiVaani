# 🌾 BhoomiVaani – Voice-Driven GenAI for Farmers

**Empowering rural farmers in India with Hindi voice-based AI for crop yield forecasting, disaster warnings, and weather alerts.**

## 🎯 Key Features

- 🗣️ Hindi speech input/output
- 🤖 LLM-based Q&A using LangChain + RAG
- 🌦️ Predictive crop and weather model integration
- 📡 Works offline with llama.cpp compatibility
- 📱 No GUI needed – runs on basic mic/phone setups

## ⚙️ Tech Stack

- Python, Whisper/Vosk (STT), gTTS/Coqui (TTS)
- LangChain + GPT or LLaMA (via llama.cpp)
- Scikit-learn/XGBoost/LightGBM for predictions
- FAISS + OpenAI Embeddings for vector retrieval

## 📁 Structure

app/
├── main.py
├── stt.py
├── tts.py
├── langchain_rag.py
├── prediction.py