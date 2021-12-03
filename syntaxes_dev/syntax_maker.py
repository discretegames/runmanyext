import csv
import json
from pathlib import Path
from itertools import islice

PATTERNS_INSERT_INDEX = 3
PATTERN_PLACEHOLDER = '<PATTERN>'
ID_PLACEHOLDER = '<ID>'
SOURCE_PLACEHOLDER = '<SOURCE>'


def load_languages(languages_csv):
    languages = []
    with open(languages_csv) as file:
        for row in islice(csv.reader(file), 1, None):
            languages.append(tuple(item.strip() for item in row))
    return languages


def make_include_object(id):
    return {'include': f'#{id}-section'}


def make_language_parts(parts_json, name, id, source):
    with open(parts_json) as file:
        content = file.read()
        content = content.replace(PATTERN_PLACEHOLDER, name)
        content = content.replace(ID_PLACEHOLDER, id)
        content = content.replace(SOURCE_PLACEHOLDER, source)
        return json.loads(content)


def insert_language_parts(syntax, include, parts, index):
    syntax['repository']['enabled-section']['patterns'].insert(index, include)
    for key, value in parts.items():
        syntax['repository'][key] = value


def save_final_json(final_json, syntax):
    final_json.parent.mkdir(parents=True, exist_ok=True)
    with open(final_json, 'w') as file:
        json.dump(syntax, file, indent=4)


def make_syntax(languages_csv, dev_syntax, parts_json, final_json):
    languages = load_languages(languages_csv)
    for index, (name, id, source) in enumerate(languages, PATTERNS_INSERT_INDEX):
        include = make_include_object(id)
        parts = make_language_parts(parts_json, name, id, source)
        insert_language_parts(dev_syntax, include, parts, index)
    save_final_json(final_json, dev_syntax)


def load_dev_syntax(dev_json, keys_to_remove, index_to_remove=PATTERNS_INSERT_INDEX):
    with open(dev_json) as file:
        dev_json = json.load(file)
    del dev_json['repository']['enabled-section']['patterns'][index_to_remove]
    for key in keys_to_remove:
        del dev_json['repository'][key]
    return dev_json


if __name__ == '__main__':
    path = Path(__file__)
    languages_csv = path.parent.with_name('supported-languages.csv')
    dev_json = path.with_name('many.tmLanguage.json')
    dev_syntax = load_dev_syntax(dev_json, ('ada-section', 'ada-snippet'))
    parts_json = path.with_name('language_parts.json')
    final_json = path.parent.parent / 'syntaxes' / 'many.tmLanguage.json'
    make_syntax(languages_csv, dev_syntax, parts_json, final_json)
