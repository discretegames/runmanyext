import csv
import json
from pathlib import Path
from itertools import islice

PATTERNS_INSERT_INDEX = 5
NAME_PLACEHOLDER = '<NAME>'
ID_PLACEHOLDER = '<ID>'
SOURCE_PLACEHOLDER = '<SOURCE>'


def load_raw_json(raw_json):
    with open(raw_json) as file:
        return json.load(file)


def load_languages(languages_csv):
    languages = []
    with open(languages_csv) as file:
        for row in islice(csv.reader(file), 1, None):
            languages.append(tuple(item.strip() for item in row))
    return languages


def make_include_object(id):
    return {'include': f'#{id}-section-list'}


def make_language_parts(parts_json, name, id, source):
    with open(parts_json) as file:
        content = file.read()
        content = content.replace(NAME_PLACEHOLDER, name)
        content = content.replace(ID_PLACEHOLDER, id)
        content = content.replace(SOURCE_PLACEHOLDER, source)
        return json.loads(content)


def insert_language_parts(syntax, include, parts, index):
    syntax['patterns'].insert(index, include)
    for key, value in parts.items():
        syntax['repository'][key] = value


def save_final_json(final_json, syntax):
    final_json.parent.mkdir(parents=True, exist_ok=True)
    with open(final_json, 'w') as file:
        json.dump(syntax, file, indent=4)


def make_syntax(languages_csv, raw_json, parts_json, final_json):
    syntax = load_raw_json(raw_json)
    languages = load_languages(languages_csv)
    for index, (name, id, source) in enumerate(languages, PATTERNS_INSERT_INDEX):
        include = make_include_object(id)
        parts = make_language_parts(parts_json, name, id, source)
        insert_language_parts(syntax, include, parts, index)
    save_final_json(final_json, syntax)


if __name__ == '__main__':
    path = Path(__file__)
    languages_csv = path.parent.with_name('supported-languages.csv')
    raw_json = path.with_name('raw.many.tmLanguage.json')
    parts_json = path.with_name('language_parts.json')
    final_json = path.parent.parent / 'syntaxes' / 'many.tmLanguage.json'
    make_syntax(languages_csv, raw_json, parts_json, final_json)
