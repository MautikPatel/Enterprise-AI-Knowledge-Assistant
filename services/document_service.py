from pathlib import Path

# Folder where uploaded documents are stored
DOCUMENTS_FOLDER = Path("data/documents")


def save_uploaded_files(uploaded_files):
    """
    Save uploaded PDF files into the documents folder.
    Returns a list of saved filenames.
    """

    DOCUMENTS_FOLDER.mkdir(parents=True, exist_ok=True)

    saved_files = []

    for uploaded_file in uploaded_files:
        destination = DOCUMENTS_FOLDER / uploaded_file.name

        with open(destination, "wb") as f:
            f.write(uploaded_file.getbuffer())

        saved_files.append(uploaded_file.name)

    return saved_files


def get_document_list():
    """
    Return all PDF documents currently stored.
    """

    DOCUMENTS_FOLDER.mkdir(parents=True, exist_ok=True)

    return sorted(DOCUMENTS_FOLDER.glob("*.pdf"))