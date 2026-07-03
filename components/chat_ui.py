import streamlit as st

from services.retriever_service import retrieve_chunks
from services.llm_service import generate_answer
from components.source_cards import show_source_cards

def show_chat():
    st.header("💬 Enterprise AI Assistant")
    col1, col2 = st.columns([8, 1])
    with col1:
        st.caption("Ask questions about your enterprise knowledge base.")
    with col2:
        if st.button("🗑️", help="Clear Chat"):
            st.session_state.messages = []
            st.rerun()

    st.divider()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask a question about your enterprise documents...")
    if not prompt:
        return

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if not st.session_state.get("knowledge_ready", False):
        answer = (
            "⚠️ Knowledge Base has not been built yet.\n\n"
            "Go to the **Administrator** tab and click **Build Knowledge Base**."
        )
        with st.chat_message("assistant"):
            st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        return

    with st.chat_message("assistant"):
        status = st.empty()
        status.info("🔍 Searching enterprise knowledge base...")
        try:
            results = retrieve_chunks(prompt)
        except Exception as ex:
            status.error(str(ex))
            return

        status.info("🧠 Generating response...")
        try:
            answer = generate_answer(prompt, results)
        except Exception as ex:
            answer = f"Unable to generate answer.\n\n{str(ex)}"
        status.empty()

        st.markdown(answer)
        show_source_cards(results)

    st.session_state.messages.append({"role": "assistant", "content": answer})