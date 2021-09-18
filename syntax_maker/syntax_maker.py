import csv
from pathlib import Path

PATH = Path(__file__)
CSV = PATH.with_name('languages.csv')
RAW = PATH.with_name('raw.many.tmLanguage.json')
PARTS = PATH.with_name('language_parts.json')
FINAL = PATH.parent.parent / 'syntaxes' / 'many.tmLanguage.json'

if __name__ == "__main__":
    with open(FINAL, 'w') as f:
        f.write("foo")

    with open(CSV) as file:
        reader = csv.reader(file)
        print(reader)
