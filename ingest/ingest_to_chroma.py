import os
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

PDF_DIR = "../data/pdfs"
CHROMA_DIR = "../chroma_db"

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory=CHROMA_DIR,
    embedding_function=embedding
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

def extract_text_with_ocr(pdf_path):
    docs = []
    pdf = fitz.open(pdf_path)

    for page_num, page in enumerate(pdf):
        text = page.get_text().strip()

        # If text is too small, OCR the page
        if len(text) < 50:
            pix = page.get_pixmap(dpi=300)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text = pytesseract.image_to_string(img)

        if text.strip():
            docs.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": os.path.basename(pdf_path),
                        "page": page_num + 1,
                        "ocr": len(text) < 50
                    }
                )
            )

    return docs


all_docs = []

for file in os.listdir(PDF_DIR):
    if file.lower().endswith(".pdf"):
        path = os.path.join(PDF_DIR, file)
        print(f"Ingesting: {file}")
        all_docs.extend(extract_text_with_ocr(path))

chunks = splitter.split_documents(all_docs)

print(f"Total chunks created: {len(chunks)}")

vectordb.add_documents(chunks)

print("✅ Ingestion complete and persisted to disk")
