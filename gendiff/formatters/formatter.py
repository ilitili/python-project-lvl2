from types import MappingProxyType

from gendiff.formatters.json import get_json
from gendiff.formatters.plain import get_plain
from gendiff.formatters.stylish import get_stylish

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'

FORMATTERS = MappingProxyType({
    STYLISH: get_stylish,
    PLAIN: get_plain,
    JSON: get_json,
})


def get_formatter(style):
    if style in FORMATTERS:
        return FORMATTERS.get(style)
    raise ValueError
