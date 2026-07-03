import streamlit as st

def show_source_cards(results):
    if not results or "documents" not in results or len(results["documents"]) == 0:
        return

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    st.markdown("### 📄 Sources")

    for document, metadata in zip(documents, metadatas):
        with st.container(border=True):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.markdown(f"**{metadata.get('filename', 'Unknown')}**")
                st.caption(f"Chunk ID: {metadata.get('chunk_id', '')}")
            with col2:
                doc_type = metadata.get("document_type", "Unknown")
                st.info(doc_type)

            with st.expander("View Retrieved Content", expanded=False):
                st.write(document)