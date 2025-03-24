from zipfile import ZipFile
from pathlib import Path

if __name__ == "__main__":
    PDFS_PATH = Path() / "pdfs"
    ZIP_PATH = Path() / "zipFiles"
    ZIP_PATH_NAME = ZIP_PATH / "pdfs.zip"

    ZIP_PATH.mkdir(exist_ok=True)

    with ZipFile(ZIP_PATH_NAME, "w") as myzip:
        for pdf in PDFS_PATH.glob("*.pdf"):
            myzip.write(pdf, pdf.name)

    print(PDFS_PATH.absolute())