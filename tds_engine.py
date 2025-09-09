import streamlit as st

def tds_ui():
    st.header("💼 TDS Filing")
    salary=st.number_input("Salary Paid (₹)",min_value=0)
    if st.button("Prepare TDS Draft"):
        tds=salary*0.1
        draft=f"Form24Q: Salary={salary}, TDS={tds}"
        st.download_button("📥 Download TDS.txt",draft,"TDS_Draft.txt")
        st.success(f"✅ TDS={tds}")
