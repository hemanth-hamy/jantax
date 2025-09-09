# -*- coding: utf-8 -*-
import sys, io, streamlit as st
import tax_engine, gst_engine, tds_engine, pt_engine, utils

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

st.set_page_config(page_title="JanTax", page_icon="🌍", layout="wide")
st.title("🌍 JanTax – Social Justice Edition")
st.sidebar.title("📌 Navigation")

pages = ["Home","Voice Assistant","ITR Filing","GST Filing","TDS Filing","PT Filing","Help","Contact"]
choice = st.sidebar.radio("Go to:", pages)

if choice=="Home":
    st.info("AI-powered Indian Tax Helper: ITR + GST + TDS + PT drafts")
elif choice=="Voice Assistant":
    utils.voice_assistant_ui()
elif choice=="ITR Filing":
    tax_engine.itr_ui()
elif choice=="GST Filing":
    gst_engine.gst_ui()
elif choice=="TDS Filing":
    tds_engine.tds_ui()
elif choice=="PT Filing":
    pt_engine.pt_ui()
elif choice=="Help":
    st.write("FAQs + Email: support@jantax.ai")
elif choice=="Contact":
    st.write("📞 +91-99999-99999")
