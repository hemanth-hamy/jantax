import streamlit as st

def pt_ui():
    st.header("🏢 PT Filing")
    employees=st.number_input("Employees",min_value=0)
    if st.button("Prepare PT Draft"):
        payable=employees*200
        st.download_button("📥 Download PT.pdf",f"Employees={employees}, PT={payable}","PT_Draft.pdf")
        st.success(f"✅ Professional Tax={payable}")
