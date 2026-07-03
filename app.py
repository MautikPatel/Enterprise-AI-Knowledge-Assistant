import streamlit as st
import ollama
from pathlib import Path
												 

from services.document_service import (
    save_uploaded_files,
    get_document_list,
)

from services.pdf_service import extract_all_pdfs
from services.chunk_service import create_chunks

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Enterprise AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🤖 Enterprise AI Knowledge Assistant")

st.markdown(
    "Ask anything. Responses are generated **locally** using **Llama 3.2** via **Ollama**."
)

st.divider()

# --------------------------------------------------
# Document Management
# --------------------------------------------------
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

st.divider()

# --------------------------------------------------
# Read PDFs & Create Chunks
# --------------------------------------------------

if st.button("📖 Read All Documents"):

    with st.spinner("Reading PDFs..."):

        documents = extract_all_pdfs(
            Path("data/documents")
        )

        chunks = create_chunks(documents)

    st.success(f"Successfully processed {len(documents)} document(s).")

    total_pages = sum(doc["pages"] for doc in documents)
    total_characters = sum(len(doc["text"]) for doc in documents)

    st.metric("Documents", len(documents))
    st.metric("Pages", total_pages)
    st.metric("Characters", total_characters)
    st.metric("Chunks", len(chunks))

    st.divider()

    st.subheader("Extracted Documents")

    for doc in documents:

        with st.expander(doc["filename"]):
            st.write(f"**Pages:** {doc['pages']}")
            st.write(f"**Characters:** {len(doc['text'])}")

            st.text(
                f"Preview (First 1500 Characters)\n\n{doc['text'][:1500]}"
            )

    st.divider()

    st.subheader("Sample Chunks")

    for chunk in chunks[:5]:

        with st.expander(
            f"{chunk['filename']} | Chunk {chunk['chunk_id']}"
        ):

            st.write(chunk["text"])
 

# --------------------------------------------------
# Ask AI
# --------------------------------------------------
st.divider()

st.subheader("💬 Ask AI")

prompt = st.text_area(
    "Enter your question",
    height=150,
    placeholder="Example: Explain what Business Intelligence is..."
)

													
		
													
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