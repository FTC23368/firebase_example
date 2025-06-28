from datetime import datetime
from io import BytesIO

import firebase_admin
from firebase_admin import credentials, firestore, storage
import streamlit as st
from PyPDF2 import PdfReader


def init_firestore():
    """Initialize and return a Firestore client using Streamlit secrets."""
    if not firebase_admin._apps:
        cred_info = st.secrets.get("firebase")
        if cred_info is None:
            raise RuntimeError("Firebase credentials not found in st.secrets")
        cred = credentials.Certificate(dict(cred_info))

        # allow overriding the bucket used for uploads
        bucket_name = cred_info.get("storage_bucket")
        if not bucket_name:
            project_id = cred_info.get("project_id")
            if not project_id:
                raise RuntimeError(
                    "project_id or storage_bucket must be provided in st.secrets"
                )
            bucket_name = project_id + ".firebasestorage.app"

        firebase_admin.initialize_app(cred, {"storageBucket": bucket_name})
    return firestore.client()


def get_bucket():
    """Return the default Firebase Storage bucket."""
    init_firestore()  # ensure app initialized
    return storage.bucket()


def extract_text(file_bytes: bytes, file_type: str) -> str:
    """Return plain text extracted from PDF or text file bytes."""
    if file_type == "application/pdf":
        reader = PdfReader(BytesIO(file_bytes))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        return text
    # assume utf-8 text for other types
    return file_bytes.decode("utf-8", errors="ignore")


def upload_file(file_bytes: bytes, filename: str, file_type: str, doc_category: list, doc_name: str):
    """Upload the file to Firebase Storage and store metadata only."""
    db = init_firestore()
    bucket = get_bucket()
    uploaded_at = datetime.utcnow()
    content_text = extract_text(file_bytes, file_type)

    # paths in storage
    file_path = f"files/{filename}"
    content_path = f"file_contents/{filename}.content"

    # upload the original file
    blob = bucket.blob(file_path)
    blob.upload_from_string(file_bytes, content_type=file_type)

    # upload extracted text as separate file
    text_blob = bucket.blob(content_path)
    text_blob.upload_from_string(content_text, content_type="text/plain")

    # metadata record with references to storage paths
    doc_ref = db.collection("files").document(filename)
    doc_ref.set(
        {
            "file_name": filename,
            "file_size": len(file_bytes),
            "file_type": file_type,
            "uploaded_at": uploaded_at,
            "storage_path": file_path,
            "content_path": content_path,
            "doc_category": doc_category,
            "doc_name": doc_name,
        }
    )


def list_files():
    """Return metadata for all uploaded files."""
    db = init_firestore()
    docs = db.collection("files").stream()
    return [doc.to_dict() for doc in docs]


def get_file_content(filename: str) -> bytes:
    """Retrieve binary content for the given filename from Storage."""
    db = init_firestore()
    bucket = get_bucket()
    meta = db.collection("files").document(filename).get()
    if meta.exists:
        storage_path = meta.to_dict().get("storage_path", f"files/{filename}")
        blob = bucket.blob(storage_path)
        if blob.exists():
            return blob.download_as_bytes()
    return b""


def get_text_content(filename: str) -> str:
    """Retrieve text content file from Storage."""
    db = init_firestore()
    bucket = get_bucket()
    meta = db.collection("files").document(filename).get()
    if meta.exists:
        content_path = meta.to_dict().get(
            "content_path", f"file_contents/{filename}.content"
        )
        blob = bucket.blob(content_path)
        if blob.exists():
            return blob.download_as_text()
    return ""
