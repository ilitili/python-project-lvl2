from gendiff.scripts.gendiff import generate_diff

import pytest


@pytest.mark.parametrize("file1,file2,expected_file,format", [(
    'tests/fixtures/plain/file1.json',
    'tests/fixtures/plain/file2.json',
    'tests/fixtures/plain/stylish',
    'stylish',
), (
    'tests/fixtures/plain/file1.yml',
    'tests/fixtures/plain/file2.yml',
    'tests/fixtures/plain/stylish',
    'stylish',
), (
    'tests/fixtures/plain/file1.yaml',
    'tests/fixtures/plain/file2.yaml',
    'tests/fixtures/plain/stylish',
    'stylish',
), (
    'tests/fixtures/nested/file1.json',
    'tests/fixtures/nested/file2.json',
    'tests/fixtures/nested/stylish',
    'stylish',
), (
    'tests/fixtures/nested/file1.yml',
    'tests/fixtures/nested/file2.yml',
    'tests/fixtures/nested/stylish',
    'stylish',
), (
    'tests/fixtures/plain/file1.json',
    'tests/fixtures/plain/file2.json',
    'tests/fixtures/plain/plain',
    'plain',
), (
    'tests/fixtures/plain/file1.yml',
    'tests/fixtures/plain/file2.yml',
    'tests/fixtures/plain/plain',
    'plain',
), (
    'tests/fixtures/nested/file1.json',
    'tests/fixtures/nested/file2.json',
    'tests/fixtures/nested/plain',
    'plain',
), (
    'tests/fixtures/nested/file1.yml',
    'tests/fixtures/nested/file2.yml',
    'tests/fixtures/nested/plain',
    'plain',
), (
    'tests/fixtures/plain/file1.json',
    'tests/fixtures/plain/file2.json',
    'tests/fixtures/plain/json',
    'json',
), (
    'tests/fixtures/plain/file1.yml',
    'tests/fixtures/plain/file2.yml',
    'tests/fixtures/plain/json',
    'json',
), (
    'tests/fixtures/nested/file1.json',
    'tests/fixtures/nested/file2.json',
    'tests/fixtures/nested/json',
    'json',
), (
    'tests/fixtures/nested/file1.yml',
    'tests/fixtures/nested/file2.yml',
    'tests/fixtures/nested/json',
    'json',
)])
def test_generate_diff(file1, file2, expected_file, format):
    with open(expected_file, 'r') as file:
        expected_data = file.read()

    assert generate_diff(file1, file2, format) == expected_data
