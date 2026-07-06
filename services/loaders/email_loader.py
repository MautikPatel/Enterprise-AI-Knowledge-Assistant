from pathlib import Path
import email
import extract_msg


def extract_eml(file_path: Path):
    """
    Extract text from EML file.
    """

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:

        msg = email.message_from_file(f)

    body = ""

    if msg.is_multipart():

        for part in msg.walk():

            if part.get_content_type() == "text/plain":

                payload = part.get_payload(decode=True)

                if payload:
                    body += payload.decode(errors="ignore")

    else:

        payload = msg.get_payload(decode=True)

        if payload:
            body = payload.decode(errors="ignore")

    return {
        "filename": file_path.name,
        "document_type": "Email",
        "pages": 1,
        "text": body
    }


def extract_msg_file(file_path: Path):
    """
    Extract text from Outlook MSG file.
    """

    msg = extract_msg.Message(file_path)

    text = f"""
Subject:
{msg.subject}

From:
{msg.sender}

Body:

{msg.body}
"""

    return {
        "filename": file_path.name,
        "document_type": "Email",
        "pages": 1,
        "text": text
    }


def extract_all_email(folder: Path):

    documents = []

    for file in folder.glob("*.eml"):
        documents.append(extract_eml(file))

    for file in folder.glob("*.msg"):
        documents.append(extract_msg_file(file))

    return documents