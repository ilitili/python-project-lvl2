from os.path import splitext

from gendiff.parsers import parse_json
from gendiff.parsers import parse_yaml
from gendiff.diff_builder import build_diff
from gendiff.formatters.formatter import STYLISH, get_formatter
from gendiff.loaders import get_loader


def read_file(filepath):
    with open(filepath) as file:
        return file.read()


def get_data(filepath):
    _, ext = splitext(filepath)
    load = get_loader(ext[1:].lower())
    if load:
        data = read_file(filepath)
        return load(data)
    raise ValueError


def generate_diff(first_file, second_file, style=STYLISH):
    file1_extension = splitext(filepath1)[1]

    if file1_extension == '.json':
        file1 = parse_json(first_file)
        file2 = parse_json(second_file)
    else:
        file1 = parse_yaml(first_file)
        file2 = parse_yaml(second_file)
        
    first_dict = get_data(file1)
    second_dict = get_data(file2)

    diff = build_diff(first_dict, second_dict)
    formatter = get_formatter(style)

    return formatter(diff)
