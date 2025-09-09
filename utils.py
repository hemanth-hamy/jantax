import streamlit as st

def voice_assistant_ui():
    st.header("🎤 Voice Assistant")
    st.write("Speak/type in Hindi/Kannada/Tamil/Telugu.")
    user_input=st.text_area("Enter/Dictate")
    if st.button("Prepare Draft"):
        if user_input:
            st.success(f"✅ Draft prepared for: {user_input}")
            st.download_button("📥 Download Draft.txt",user_input,"Voice_Draft.txt")
        else:
            st.warning("Provide input first.")
