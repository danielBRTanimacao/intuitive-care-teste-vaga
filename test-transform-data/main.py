from pathlib import Path
from pypdf import PdfReader

if __name__ == "__main__":
    PDF = Path() / "pdfs" / "Anexo1.pdf"
    ZIP_PATH = Path() / 

    pdf_reader = PdfReader(PDF)
    print(pdf_reader.get_num_pages())
