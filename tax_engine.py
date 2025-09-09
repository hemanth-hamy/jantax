import streamlit as st, json

def compute_tax(income,deductions,regime="old"):
    taxable=max(0,income-deductions)
    tax=0
    if regime=="old":
        if taxable<=250000: tax=0
        elif taxable<=500000: tax=(taxable-250000)*0.05
        elif taxable<=1000000: tax=12500+(taxable-500000)*0.2
        else: tax=112500+(taxable-1000000)*0.3
    else: # simplified new regime
        if taxable<=300000: tax=0
        elif taxable<=600000: tax=(taxable-300000)*0.05
        elif taxable<=900000: tax=15000+(taxable-600000)*0.1
        elif taxable<=1200000: tax=45000+(taxable-900000)*0.15
        elif taxable<=1500000: tax=90000+(taxable-1200000)*0.2
        else: tax=150000+(taxable-1500000)*0.3
    return taxable,tax

def itr_ui():
    st.header("🧾 ITR Filing")
    income=st.number_input("Annual Income (₹)",min_value=0)
    deductions=st.number_input("Deductions (₹)",min_value=0)
    regime=st.selectbox("Regime",["old","new"])
    if st.button("Prepare ITR Draft"):
        taxable,tax=compute_tax(income,deductions,regime)
        draft={"Income":income,"Deductions":deductions,"Regime":regime,"Taxable":taxable,"Tax":tax}
        st.download_button("📥 Download ITR.json",json.dumps(draft),"ITR_Draft.json")
        st.success(f"✅ Taxable={taxable}, Tax={tax}")
