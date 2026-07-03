from pathlib import Path
from PIL import Image
import pytesseract


def extract_image(file_path: Path):
    """
    Extract text from image using OCR.
    """

    image = Image.open(file_path)

    text = pytesseract.image_to_string(image)

    return {
        "filename": file_path.name,
        "document_type": "Image",
        "pages": 1,
        "text": text
    }


def extract_all_images(folder: Path):

    documents = []

    for extension in ["*.png", "*.jpg", "*.jpeg"]:

        for file in folder.glob(extension):

            documents.append(
                extract_image(file)
            )

    return documents