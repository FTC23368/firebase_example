# Streamlit Firebase Example

This repository contains a simple Streamlit application with multiple pages. The app demonstrates how to upload PDF or text files to Firebase Storage and view the uploaded files. Metadata about each upload is stored in Firestore.

## Requirements

- Python 3.9+
- Streamlit
- firebase-admin
- PyPDF2

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running the App

Run the Streamlit application from the project root:

```bash
streamlit run Home.py
```

Streamlit will automatically detect the additional pages in the `pages/` directory.

## Firebase Setup

Provide your Firebase service account details in `.streamlit/secrets.toml`. The
credentials should be placed under the `firebase` section:

```toml
[firebase]
type = "service_account"
project_id = "your-project-id"
private_key_id = "..."
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "..."
client_id = "..."
token_uri = "https://oauth2.googleapis.com/token"
# Optional: specify a bucket name if different from "<project_id>.firebasestorage.app"
storage_bucket = "your-custom-bucket-name"
```

Streamlit automatically loads these secrets and the app will use them to
initialize Firebase.

The application expects a Cloud Storage bucket to exist. By default the bucket
name is assumed to be `<project_id>.firebasestorage.app`. If your bucket uses a
different name, provide it via the optional `storage_bucket` field shown above.

## Setting up Firebase Storage and Firestore

1. Create a Firebase project at <https://console.firebase.google.com/>.
2. In the **Firestore Database** section, create a database in production or test mode.
3. In the **Storage** section, create a Cloud Storage bucket. A bucket named
   `<project_id>.firebasestorage.app` is normally created automatically when you
   enable storage.

## Getting the secrets.toml configuration

1. Open your project settings and select **Service accounts**.
2. Click **Generate new private key** to download a JSON credentials file.
3. Copy the values from that file into the `[firebase]` section of
   `.streamlit/secrets.toml` as shown above.
4. Add a `storage_bucket` entry if your bucket name differs from the default.

