import streamlit as st

from services.document_loader import get_loaded_documents
from services.chunk_service import create_chunks


_TYPE_BADGE_COLORS = {
    "pdf": ("#fee2e2", "#b91c1c"),
    "word": ("#dbeafe", "#1d4ed8"),
    "docx": ("#dbeafe", "#1d4ed8"),
    "excel": ("#dcfce7", "#15803d"),
    "xlsx": ("#dcfce7", "#15803d"),
    "pptx": ("#fef3c7", "#b45309"),
    "csv": ("#e0e7ff", "#4338ca"),
    "txt": ("#f3f4f6", "#374151"),
}


def _type_badge(document_type):
    key = str(document_type).lower()
    bg, fg = _TYPE_BADGE_COLORS.get(key, ("#f3f4f6", "#374151"))
    st.markdown(
        f"""
        <span style="
            background:{bg};
            color:{fg};
            padding:3px 10px;
            border-radius:6px;
            font-size:12.5px;
            font-weight:600;">
            {document_type}
        </span>
        """,
        unsafe_allow_html=True,
    )


def show_document_inventory():
    """
    Display all indexed enterprise documents.
    """

    documents = get_loaded_documents()

    if not documents:
        st.info("No enterprise documents found.")
        return

    chunks = create_chunks(documents)

    chunk_lookup = {}

    for chunk in chunks:

        filename = chunk["filename"]

        chunk_lookup[filename] = (
            chunk_lookup.get(filename, 0) + 1
        )

    st.markdown(
        '<div style="font-size:18px;font-weight:700;color:#111827;">'
        "📂 Enterprise Document Inventory</div>",
        unsafe_allow_html=True,
    )

    st.caption(
        f"{len(documents)} document(s) available."
    )

    with st.container(border=True):

        header = st.columns([5, 1.2, 1, 1, 1.5])

        header[0].markdown("**Document**")
        header[1].markdown("**Type**")
        header[2].markdown("**Pages**")
        header[3].markdown("**Chunks**")
        header[4].markdown("**Status**")

        st.divider()

        for document in documents:

            filename = document["filename"]

            row = st.columns([5, 1.2, 1, 1, 1.5])

            row[0].markdown(f"📄 {filename}")

            with row[1]:
                _type_badge(document["document_type"])

            row[2].markdown(
                str(document["pages"])
            )

            row[3].markdown(
                str(
                    chunk_lookup.get(
                        filename,
                        0
                    )
                )
            )

            row[4].success("Indexed")
