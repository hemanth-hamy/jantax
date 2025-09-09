import streamlit as st, requests, os

BASE_URL = os.getenv("BASE_URL","http://localhost:8000")
st.set_page_config(page_title="JanTax", page_icon="🌍", layout="wide")
st.title("🌍 JanTax – Social Justice Edition")

choice = st.sidebar.radio("Choose Module",["Home","Voice","ITR","GST","TDS","PT","Help","Contact"])

if choice=="Home":
    st.info("AI-powered Indian Tax Helper: ITR + GST + TDS + PT")
elif choice=="Voice":
    st.header("🎤 Voice Assistant")
    st.write("Upload voice in Hindi/Kannada/Tamil/Telugu")
    file=st.file_uploader("Upload voice",type=["wav","mp3"])
    if file and st.button("Transcribe + Draft"):
        res=requests.post(f"{BASE_URL}/voice",files={"file":file.getvalue()})
        st.json(res.json())
elif choice=="ITR":
    st.header("🧾 ITR Filing")
    inc=st.number_input("Income",0)
    ded=st.number_input("Deductions",0)
    reg=st.selectbox("Regime",["old","new"])
    if st.button("Prepare ITR Draft"):
        res=requests.post(f"{BASE_URL}/itrfiling",json={"income":inc,"deductions":ded,"regime":reg})
        st.json(res.json())
elif choice=="GST":
    st.header("💰 GST Filing")
    sales=st.number_input("Sales",0)
    purchases=st.number_input("Purchases",0)
    if st.button("Prepare GST Draft"):
        res=requests.post(f"{BASE_URL}/gstfiling",json={"sales":sales,"purchases":purchases})
        st.json(res.json())
elif choice=="TDS":
    st.header("💼 TDS Filing")
    salary=st.number_input("Salary",0)
    if st.button("Prepare TDS Draft"):
        res=requests.post(f"{BASE_URL}/tdsfiling",json={"salary":salary})
        st.json(res.json())
elif choice=="PT":
    st.header("🏢 PT Filing")
    employees=st.number_input("Employees",0)
    if st.button("Prepare PT Draft"):
        res=requests.post(f"{BASE_URL}/ptfiling",json={"employees":employees})
        st.json(res.json())
elif choice=="Help":
    st.write("FAQs: support@jantax.ai")
elif choice=="Contact":
    st.write("📞 +91-99999-99999")
