from flask import Flask, jsonify
from pathlib import Path
from utils.reader import reader_csv

app = Flask(__name__)

ROOT_FILE = Path(__name__).parent

@app.route("/api", method=["GET"])
def get_texts():
    CSV_FILE = ROOT_FILE / "csvs" / "Relatorio_cadop.csv"
    response = reader_csv(CSV_FILE)
    return jsonify(response)

app.run(debug=True)