from types import MappingProxyType

from gendiff.diff_builder import ADDED, CHANGED, EMBEDDED, REMOVED, UNCHANGED
from gendiff.formatters.stylish import CORRECT_VALUES

HANDLERS = MappingProxyType({
    ADDED: lambda key, value, _: "Property '{0}' was added with value: {1}".format(key, format_value(value)),
    REMOVED: lambda key, _, __: "Property '{0}' was removed".format(key),
    CHANGED: lambda key, value, _:
        "Property '{0}' was updated. From {1} to {2}".format(key, format_value(value[0]), format_value(value[1])),
    UNCHANGED: lambda _, __, ___: '',
    EMBEDDED: lambda key, value, func: func(value, key),
})


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'

    elif value is None or isinstance(value, bool):
        return CORRECT_VALUES.get(value)

    elif isinstance(value, str):
        return "'{0}'".format(value)

    return value


def get_plain(diff, start_key=''):
    lines = []
    for type_name, key, value in diff:
        handler = HANDLERS.get(type_name)
        full_key = '{0}.{1}'.format(start_key, key) if start_key else key
        line = handler(full_key, value, get_plain)
        lines.append(line)

    return '\n'.join(filter(lambda item: item, lines))
