import streamlit as st


_TYPE_ICONS = {
    "pdf": "📕",
    "word": "📘",
    "docx": "📘",
    "excel": "📗",
    "xlsx": "📗",
    "pptx": "📙",
    "csv": "📊",
    "txt": "📄",
}


def _type_icon(document_type):
    return _TYPE_ICONS.get(str(document_type).lower(), "📄")


def show_source_cards(results):
    """
    Display the retrieved source documents used to generate the answer.
    """

    if (
        not results
        or "documents" not in results
        or len(results["documents"]) == 0
    ):
        return

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    # -----------------------------------------
    # Group chunks by filename
    # -----------------------------------------

    grouped_sources = {}

    for document, metadata in zip(documents, metadatas):

        filename = metadata.get("filename", "Unknown")

        if filename not in grouped_sources:

            grouped_sources[filename] = {
                "document_type": metadata.get(
                    "document_type",
                    "Unknown"
                ),
                "chunks": [],
            }

        grouped_sources[filename]["chunks"].append(
            {
                "chunk_id": metadata.get(
                    "chunk_id",
                    ""
                ),
                "text": document,
            }
        )

    # -----------------------------------------
    # UI
    # -----------------------------------------

    st.markdown("---")

    st.markdown(
        '<div style="font-size:18px;font-weight:700;color:#111827;">📚 Sources Used</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        f"{len(grouped_sources)} document(s) contributed to this answer."
    )

    # -----------------------------------------
    # Source Cards
    # -----------------------------------------

    for filename, info in grouped_sources.items():

        with st.container(border=True):

            col1, col2 = st.columns([5, 1])

            with col1:

                st.markdown(
                    f"**{_type_icon(info['document_type'])} {filename}**"
                )

                st.caption(
                    f"{len(info['chunks'])} Retrieved Chunk(s)"
                )

            with col2:

                st.success(
                    info["document_type"]
                )

            preview = info["chunks"][0]["text"][:250]

            st.write(
                preview + "..."
                if len(preview) == 250
                else preview
            )

            with st.expander(
                "View Retrieved Chunks"
            ):

                for chunk in info["chunks"]:

                    st.markdown(
                        f"**Chunk {chunk['chunk_id']}**"
                    )

                    st.write(
                        chunk["text"]
                    )

                    st.divider()
