import streamlit as st

# Configure the page (must be the first Streamlit command)
st.set_page_config(
    page_title="Enterprise AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise AI Knowledge Assistant")

st.success("✅ Congratulations! Your AI application is running successfully.")

st.markdown("---")

st.subheader("Project Information")

st.write("**Project:** Enterprise AI Knowledge Assistant")
st.write("**Version:** 1.0.0")
st.write("**Developer:** Mautik Patel")

st.info("Next, we'll integrate a local AI model using Ollama.")