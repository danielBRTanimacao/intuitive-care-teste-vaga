from flask import Flask
from pathlib import Path
from utils.reader import reader_csv

app = Flask(__name__)

@app.route("/api")
def get_texts():
    CSV_FILE = Path() / "csv" / "Relatorio_cadop.csv"
    print(CSV_FILE)
    print(reader_csv(CSV_FILE))
    return "Hello, World!"

app.run()