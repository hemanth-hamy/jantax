import streamlit as st
import requests

BASE = "https://jantax.onrender.com"

st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "ITR Filing", "GST Filing", "TDS Filing", "PT Filing", "Voice Assistant"])

st.title("🌍 JanTax – Social Justice Edition")
st.write("AI-powered Indian Tax Helper: ITR + GST + TDS + PT drafts + Voice")

def download_file(path, label):
    with open(path, "rb") as f:
        st.download_button(label, f, file_name=path)

if page == "Home":
    st.info("Welcome to JanTax Ultimate. Choose a filing tab.")

elif page == "ITR Filing":
    income = st.number_input("Income", min_value=0)
    deductions = st.number_input("Deductions", min_value=0)
    if st.button("Prepare ITR Draft"):
        r = requests.post(BASE + "/draft/itr", json={"income": income, "deductions": deductions})
        data = r.json()
        st.json(data)
        download_file("ITR_DRAFT.csv", "⬇️ Download CSV")
        download_file("ITR_DRAFT.txt", "⬇️ Download TXT")
        download_file("ITR_DRAFT.pdf", "⬇️ Download PDF")

elif page == "GST Filing":
    if st.button("Prepare GST Draft"):
        r = requests.post(BASE + "/draft/gst")
        data = r.json()
        st.json(data)
        download_file("GST_DRAFT.csv", "⬇️ Download CSV")
        download_file("GST_DRAFT.txt", "⬇️ Download TXT")
        download_file("GST_DRAFT.pdf", "⬇️ Download PDF")

elif page == "TDS Filing":
    if st.button("Prepare TDS Draft"):
        r = requests.post(BASE + "/draft/tds")
        data = r.json()
        st.json(data)
        download_file("TDS_DRAFT.csv", "⬇️ Download CSV")
        download_file("TDS_DRAFT.txt", "⬇️ Download TXT")
        download_file("TDS_DRAFT.pdf", "⬇️ Download PDF")

elif page == "PT Filing":
    if st.button("Prepare PT Draft"):
        r = requests.post(BASE + "/draft/pt")
        data = r.json()
        st.json(data)
        download_file("PT_DRAFT.csv", "⬇️ Download CSV")
        download_file("PT_DRAFT.txt", "⬇️ Download TXT")
        download_file("PT_DRAFT.pdf", "⬇️ Download PDF")

elif page == "Voice Assistant":
    st.info("Upload a voice file (WAV/MP3) to transcribe.")
    audio_file = st.file_uploader("Upload voice", type=["wav", "mp3"])
    if audio_file and st.button("Transcribe"):
        files = {"file": audio_file.getvalue()}
        r = requests.post(BASE + "/voice", files=files)
        st.json(r.json())
