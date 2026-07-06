from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(documents):
    """
    Split extracted documents into semantic chunks.
    """

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1200,

        chunk_overlap=250,

        separators=[
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            ";",
            ",",
            " ",
            ""
        ],

        length_function=len,
    )

    chunks = []

    for document in documents:

        text_chunks = splitter.split_text(
            document["text"]
        )

        for index, chunk in enumerate(
            text_chunks,
            start=1
        ):

            chunks.append(

                {
                    "filename": document["filename"],

                    "document_type": document.get(
                        "document_type",
                        "Unknown"
                    ),

                    "pages": document.get(
                        "pages",
                        1
                    ),

                    "chunk_id": index,

                    "text": chunk,
                }

            )

    return chunks