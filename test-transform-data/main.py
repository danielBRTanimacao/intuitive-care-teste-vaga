from pathlib import Path
from zipfile import ZipFile
import csv
import tabula

PDF = Path() / "pdfs" / "Anexo1.pdf"
DIRECTORY_CSV = Path() / "csvs"
CSV_FILE = DIRECTORY_CSV / "rol-procedimentos-em-saude.csv"
DIRECTORY_ZIP = Path() / "zipFiles"

your_name = "Daniel"  # Pode alterar o nome
ZIP_NAME = DIRECTORY_ZIP / f"Teste_{your_name}.zip"

abbreviations = {
    'OD': 'Seg. Odontológica',
    'AMB': 'Seg. Ambulatorial'
}

DIRECTORY_CSV.mkdir(exist_ok=True)
DIRECTORY_ZIP.mkdir(exist_ok=True)

if __name__ == "__main__":
    TABLES_PDF = tabula.read_pdf(PDF, pages='3')

    for table in TABLES_PDF:
        print(table)
        
