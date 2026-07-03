from pathlib import Path
from docx import Document


def extract_docx(file_path: Path):
    """
    Extract text from a Microsoft Word document.
    """

    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:

        text = paragraph.text.strip()

        if text:
            paragraphs.append(text)

    full_text = "\n".join(paragraphs)

    return {
        "filename": file_path.name,
        "document_type": "Word",
        "pages": 1,
        "text": full_text
    }


def extract_all_docx(folder: Path):

    documents = []

    for file in folder.glob("*.docx"):
        documents.append(extract_docx(file))

    return documents