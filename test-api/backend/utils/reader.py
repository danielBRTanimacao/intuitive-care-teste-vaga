import csv
from pathlib import Path

def reader_csv(file: Path) -> list[dict]:
    with file.open(mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        return [row for row in reader]
