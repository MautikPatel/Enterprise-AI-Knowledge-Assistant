import fitz
from pathlib import Path


def extract_text_from_pdf(pdf_path: Path):
    """
    Extract text from a single PDF.
    """

    document = fitz.open(pdf_path)

    extracted_text = []

    total_pages = document.page_count

    for page in document:
        extracted_text.append(page.get_text())

    document.close()

    return {
        "filename": pdf_path.name,
        "pages": total_pages,
        "text": "\n".join(extracted_text)
    }


def extract_all_pdfs(documents_folder: Path):
    """
    Read every PDF from the documents folder.
    """

    results = []

    pdf_files = sorted(documents_folder.glob("*.pdf"))

    for pdf in pdf_files:
        results.append(extract_text_from_pdf(pdf))

    return results