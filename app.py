import streamlit as st
import ollama

from services.document_service import (
    save_uploaded_files,
    get_document_list,
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Enterprise AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

st.subheader("📂 Enterprise Documents")

documents = get_document_list()

st.write(f"**Documents Available:** {len(documents)}")

uploaded_files = st.file_uploader(
    "Upload one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True,
)

if uploaded_files:

    if st.button("Save Documents"):

        saved = save_uploaded_files(uploaded_files)

        st.success(f"{len(saved)} document(s) uploaded successfully!")

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🤖 Enterprise AI Knowledge Assistant")

st.markdown(
    "Ask anything. Responses are generated **locally** using **Llama 3.2** via **Ollama**."
)

st.divider()

# --------------------------------------------------
# User Input
# --------------------------------------------------
prompt = st.text_area(
    "Enter your question",
    height=150,
    placeholder="Example: Explain what Business Intelligence is..."
)

# --------------------------------------------------
# Ask AI
# --------------------------------------------------
if st.button("Ask AI", use_container_width=True):

    if prompt.strip() == "":
        st.warning("Please enter a question.")
    else:

        with st.spinner("Thinking..."):

            response = ollama.chat(
                model="llama3.2:3b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.success("Response")

        st.write(response["message"]["content"])