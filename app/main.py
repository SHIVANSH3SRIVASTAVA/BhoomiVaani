from stt import transcribe_hindi
from tts import speak_hindi
from langchain_rag import ask_llm
from prediction import predict_crop, predict_weather

def main():
    text = transcribe_hindi()
    if "fasal" in text:
        answer = predict_crop()
    elif "barsaat" in text:
        answer = predict_weather()
    else:
        answer = ask_llm(text)
    speak_hindi(answer)

if __name__ == "__main__":
    main()
