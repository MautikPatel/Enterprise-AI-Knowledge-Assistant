from pathlib import Path

# --------------------------------------------------
# Documents Folder
# --------------------------------------------------

DOCUMENTS_FOLDER = Path("data/documents")

# --------------------------------------------------
# Supported File Types
# --------------------------------------------------

SUPPORTED_EXTENSIONS = [
    "*.pdf",
    "*.docx",
    "*.pptx",
    "*.xlsx",
    "*.txt",
    "*.csv",
    "*.eml",
    "*.png",
    "*.jpg",
    "*.jpeg",
]

# --------------------------------------------------
# Save Uploaded Files
# --------------------------------------------------

def save_uploaded_files(uploaded_files):
    """
    Save uploaded documents into the documents folder.
    Returns a list of saved filenames.
    """

    DOCUMENTS_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    saved_files = []

    for uploaded_file in uploaded_files:

        destination = DOCUMENTS_FOLDER / uploaded_file.name

        with open(destination, "wb") as file:

            file.write(
                uploaded_file.getbuffer()
            )

        saved_files.append(
            uploaded_file.name
        )

    return saved_files


# --------------------------------------------------
# Get All Documents
# --------------------------------------------------

def get_document_list():
    """
    Return every supported document in the
    documents folder.
    """

    DOCUMENTS_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    documents = []

    for extension in SUPPORTED_EXTENSIONS:

        documents.extend(
            DOCUMENTS_FOLDER.glob(extension)
        )

    return sorted(
        documents,
        key=lambda file: file.name.lower()
    )