from pathlib import Path


def extract_txt(file_path: Path):
    """
    Extract text from TXT file.
    """

    text = file_path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    return {
        "filename": file_path.name,
        "document_type": "Text",
        "pages": 1,
        "text": text
    }


def extract_all_txt(folder: Path):

    documents = []

    for file in folder.glob("*.txt"):
        documents.append(extract_txt(file))

    return documents