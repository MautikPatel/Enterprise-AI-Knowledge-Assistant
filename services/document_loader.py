from pathlib import Path

from services.loaders.pdf_loader import extract_all_pdfs
from services.loaders.docx_loader import extract_all_docx
from services.loaders.pptx_loader import extract_all_pptx
from services.loaders.xlsx_loader import extract_all_xlsx
from services.loaders.txt_loader import extract_all_txt
from services.loaders.csv_loader import extract_all_csv
from services.loaders.email_loader import extract_all_email
from services.loaders.image_loader import extract_all_images


def load_all_documents(folder: Path):
    """
    Load every supported document type.
    """

    documents = []

    documents.extend(extract_all_pdfs(folder))
    documents.extend(extract_all_docx(folder))
    documents.extend(extract_all_pptx(folder))
    documents.extend(extract_all_xlsx(folder))
    documents.extend(extract_all_txt(folder))
    documents.extend(extract_all_csv(folder))
    documents.extend(extract_all_email(folder))
    documents.extend(extract_all_images(folder))

    return documents