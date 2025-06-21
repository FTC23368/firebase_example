import base64
from datetime import datetime
from io import BytesIO

import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st
from PyPDF2 import PdfReader


def init_firestore():
    """Initialize and return a Firestore client using Streamlit secrets."""
    if not firebase_admin._apps:
        cred_info = st.secrets.get("firebase")
        if cred_info is None:
            raise RuntimeError("Firebase credentials not found in st.secrets")
        cred = credentials.Certificate(dict(cred_info))
        firebase_admin.initialize_app(cred)
    return firestore.client()


def extract_text(file_bytes: bytes, file_type: str) -> str:
    """Return plain text extracted from PDF or text file bytes."""
    if file_type == "application/pdf":
        reader = PdfReader(BytesIO(file_bytes))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        return text
    # assume utf-8 text for other types
    return file_bytes.decode("utf-8", errors="ignore")


def upload_file(file_bytes: bytes, filename: str, file_type: str):
    """Upload the file to Firestore and store metadata."""
    db = init_firestore()
    uploaded_at = datetime.utcnow()
    content_text = extract_text(file_bytes, file_type)

    encoded = base64.b64encode(file_bytes).decode("utf-8")

    # metadata record
    doc_ref = db.collection("files").document(filename)
    doc_ref.set({
        "file_name": filename,
        "file_size": len(file_bytes),
        "file_type": file_type,
        "uploaded_at": uploaded_at,
        "content_file": f"{filename}.content"
    })

    # store binary content
    doc_ref.collection("data").document("binary").set({"content": encoded})

    # second file with plain text
    db.collection("file_contents").document(f"{filename}.content").set({
        "text": content_text,
        "source_file": filename,
        "uploaded_at": uploaded_at
    })


def list_files():
    """Return metadata for all uploaded files."""
    db = init_firestore()
    docs = db.collection("files").stream()
    return [doc.to_dict() for doc in docs]


def get_file_content(filename: str) -> bytes:
    """Retrieve binary content for the given filename."""
    db = init_firestore()
    doc = db.collection("files").document(filename).collection("data").document("binary").get()
    if doc.exists:
        encoded = doc.to_dict().get("content", "")
        return base64.b64decode(encoded)
    return b""


def get_text_content(filename: str) -> str:
    """Retrieve text from the .content document."""
    db = init_firestore()
    doc = db.collection("file_contents").document(f"{filename}.content").get()
    if doc.exists:
        return doc.to_dict().get("text", "")
    return ""

