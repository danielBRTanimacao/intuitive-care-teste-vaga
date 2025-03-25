from pathlib import Path
from zipfile import ZipFile
from bs4 import BeautifulSoup
import requests

URL_GOV = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

DIRECTORY_PDFS = Path() / "pdfs"
DIRECTORY_ZIP = Path() / "zipFiles"
ZIP_PATH_NAME = DIRECTORY_ZIP / "pdfs.zip"

if __name__ == "__main__":
    response = requests.get(URL_GOV)
    raw_html = response.text
    parsed_html = BeautifulSoup(raw_html, "html.parser")

    URL_ATTACHMENT_1 = parsed_html.select_one("#cfec435d-6921-461f-b85a-b425bc3cb4a5 > div:nth-child(1) > ol:nth-child(3) > li:nth-child(1) > a:nth-child(1)")
    URL_ATTACHMENT_2 = parsed_html.select_one("#cfec435d-6921-461f-b85a-b425bc3cb4a5 > div:nth-child(1) > ol:nth-child(3) > li:nth-child(2) > a:nth-child(1)")

    list_url_attachments = [URL_ATTACHMENT_1["href"], URL_ATTACHMENT_2["href"]]

    DIRECTORY_PDFS.mkdir(exist_ok=True)

    for key, url in enumerate(list_url_attachments, start=1):
        res = requests.get(url)
        if res.status_code == 200:
            dir_path = DIRECTORY_PDFS / f"Anexo{key}.pdf"
            with open(dir_path, "wb") as file:
                file.write(res.content)
            print(f"Arquivo foi salvo em {dir_path.name}")
        else:
            print(f"Houve problema ao acessar url {url}\nErro: {res.status_code}")

    DIRECTORY_ZIP.mkdir(exist_ok=True)

    with ZipFile(ZIP_PATH_NAME, "w") as myzip:
        for pdf in DIRECTORY_PDFS.glob("*.pdf"):
            myzip.write(pdf, pdf.name)

    print(f"Diretorio {DIRECTORY_ZIP.absolute()} criado com sucesso!")
