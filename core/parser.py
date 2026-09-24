import io
from typing import Optional

def extract_text_from_file(file_bytes: bytes, filename: str) -> str:
    """Extracts raw text from uploaded PDF or TXT contracts."""
    if filename.lower().endswith(".txt"):
        return file_bytes.decode("utf-8", errors="replace")

    elif filename.lower().endswith(".pdf"):
        try:
            import pypdf
            reader = pypdf.PdfReader(io.BytesIO(file_bytes))
            text_pages = []
            for i, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    text_pages.append(f"--- Page {i+1} ---\n{page_text}")
            return "\n\n".join(text_pages)
        except Exception as e:
            raise ValueError(f"Failed to parse PDF document: {str(e)}")

    else:
        raise ValueError(f"Unsupported file format: {filename}. Please upload .pdf or .txt file.")
