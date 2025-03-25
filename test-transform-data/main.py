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

def replace_abbreviations(df):
    if 'OD' in df.columns: df['OD'] = df['OD'].replace(abbreviations)
    if 'AMB' in df.columns: df['AMB'] = df['AMB'].replace(abbreviations)
    return df

def save_to_csv(tables_pdf_updated, csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        csv_write = csv.writer(file)
        
        if tables_pdf_updated:
            header = tables_pdf_updated[0].columns.tolist()
            csv_write.writerow(header)
        
        for df in tables_pdf_updated:
            for row in df.values:
                csv_write.writerow(row)

def create_zip(csv_file, zip_name):
    with ZipFile(zip_name, 'w') as zipf:
        zipf.write(csv_file, csv_file.name)

if __name__ == "__main__":
    tables_pdf = tabula.read_pdf(PDF, pages='3-181')

    tables_pdf_updated = [replace_abbreviations(df) for df in tables_pdf]

    save_to_csv(tables_pdf_updated, CSV_FILE)
    create_zip(CSV_FILE, ZIP_NAME)

    print(f"O arquivo CSV foi salvo {CSV_FILE} e compactado em {ZIP_NAME}")
