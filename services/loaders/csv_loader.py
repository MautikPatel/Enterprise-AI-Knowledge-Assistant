from pathlib import Path
import pandas as pd


def extract_csv(file_path: Path):
    """
    Extract text from CSV file.
    """

    df = pd.read_csv(file_path)

    text = df.to_string(index=False)

    return {
        "filename": file_path.name,
        "document_type": "CSV",
        "pages": 1,
        "text": text
    }


def extract_all_csv(folder: Path):

    documents = []

    for file in folder.glob("*.csv"):
        documents.append(extract_csv(file))

    return documents