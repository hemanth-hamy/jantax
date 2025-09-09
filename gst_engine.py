import streamlit as st, pandas as pd

def gst_ui():
    st.header("💰 GST Filing")
    sales=st.number_input("Sales (₹)",min_value=0)
    purchases=st.number_input("Purchases (₹)",min_value=0)
    if st.button("Prepare GST Draft"):
        gst=(sales-purchases)*0.18
        df=pd.DataFrame({"Sales":[sales],"Purchases":[purchases],"GST":[gst]})
        st.download_button("📥 Download GST.csv",df.to_csv(index=False),"GST_Draft.csv")
        st.success(f"✅ GST Payable: ₹{gst}")
