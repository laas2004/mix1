import pdfplumber # type: ignore
from pdf2image import convert_from_path # type: ignore
import pytesseract # type: ignore

POPPLER_PATH = r"C:\poppler\poppler-25.12.0\Library\bin"

def extract_mixed_pdf(pdf_path):
    pages = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()

            if text and len(text.strip()) > 100:
                pages.append({
                    "page": i + 1,
                    "text": text,
                    "method": "text"
                })
            else:
                try:
                    images = convert_from_path(
                        pdf_path,
                        first_page=i + 1,
                        last_page=i + 1,
                        dpi=300,
                        poppler_path=POPPLER_PATH,
                        fmt="png",
                        use_pdftocairo=True
                    )
                    ocr_text = pytesseract.image_to_string(images[0], lang="eng")

                except Exception as e:
                    print(f"OCR failed on page {i+1}: {e}")
                    ocr_text = ""

                pages.append({
                    "page": i + 1,
                    "text": ocr_text,
                    "method": "ocr"
                })

    return pages
