from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(documents):
    """
    Split extracted document text into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )

    chunks = []

    for document in documents:

        text_chunks = splitter.split_text(document["text"])

        for index, chunk in enumerate(text_chunks, start=1):

            chunks.append(
                {
                    "filename": document["filename"],
                    "chunk_id": index,
                    "text": chunk,
                }
            )

    return chunks