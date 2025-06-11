
import streamlit as st
import os
from gtts import gTTS
from io import BytesIO
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import speech_recognition as sr

# LangChain RAG setup
def setup_langchain():
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local("vectorstore", embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 3})
    qa = RetrievalQA.from_chain_type(llm=OpenAI(temperature=0.3), retriever=retriever)
    return qa

# GenAI response function
def process_query(text):
    try:
        qa_chain = setup_langchain()
        return qa_chain.run(text)
    except Exception as e:
        return f"GenAI error: {str(e)}"

# Text-to-Speech
def text_to_speech(text):
    tts = gTTS(text=text, lang='hi')
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    return mp3_fp

# Voice Input
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Kripya boliye... (Listening in Hindi)")
        audio = r.listen(source, timeout=5)
    try:
        text = r.recognize_google(audio, language='hi-IN')
        return text
    except sr.UnknownValueError:
        return "⚠️ Awaaz samajh mein nahi aayi. Dobara koshish karein."
    except sr.RequestError:
        return "❌ Google Speech service ka access nahi mila."

# Streamlit UI
st.set_page_config(page_title="BhoomiVaani", page_icon="🌾")
st.title("🌾 BhoomiVaani – Hindi Voice GenAI for Farmers")
st.markdown("Poochein Hindi mein apna sawaal, aur BhoomiVaani de jawaab! ✨")

# Input options
input_mode = st.radio("🗣️ Prashn kaise dein?", ("Type karo", "Bol kar poochho"))
query = ""

if input_mode == "Type karo":
    query = st.text_input("📥 Aapka Prashn:")
else:
    if st.button("🎙️ Mic se bolo"):
        query = recognize_speech()
        st.text_area("📝 Pahchana gaya prashn:", value=query, height=100)

# Submit button
if st.button("🔍 Jawaab Deejiye"):
    if query:
        response = process_query(query)
        st.success(f"🤖 BhoomiVaani: {response}")
        st.audio(text_to_speech(response), format="audio/mp3")
    else:
        st.warning("Kripya prashn dein.")
