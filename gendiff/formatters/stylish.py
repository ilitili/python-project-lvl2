from types import MappingProxyType

from gendiff.diff_builder import ADDED, CHANGED, EMBEDDED, REMOVED, UNCHANGED

INDENT = '  '
DEPTH_INDENT = INDENT * 2

ADDED_FLAG = '+'
REMOVED_FLAG = '-'

HANDLERS = MappingProxyType({
    ADDED: lambda key, value, indent, _:
        get_styled_string(indent, key, value, ADDED_FLAG),
    REMOVED: lambda key, value, indent, _:
        get_styled_string(indent, key, value, REMOVED_FLAG),
    CHANGED: lambda key, value, indent, _: '\n'.join([
        get_styled_string(indent, key, value[0], REMOVED_FLAG),
        get_styled_string(indent, key, value[1], ADDED_FLAG),
    ]),
    UNCHANGED: lambda key, value, indent, _:
        get_styled_string(indent, key, value),
    EMBEDDED: lambda key, value, indent, func:
        get_styled_string(indent, key, func(value, indent + INDENT)),
})


CORRECT_VALUES = MappingProxyType({
    True: 'true',
    False: 'false',
    None: 'null',
})


def get_styled_string(indent, key, value, flag=' '):
    return '{0}{1} {2}: {3}'.format(indent, flag, key, to_string(value, indent))


def get_styled_dict(value, indent):
    lines = []
    for key in value.keys():
        line = get_styled_string(indent + DEPTH_INDENT, key, value[key])
        lines.append(line)
    return '{{\n{0}\n  {1}}}'.format('\n'.join(lines), indent)


def to_string(value, indent):
    if isinstance(value, dict):
        return get_styled_dict(value, indent)

    elif value is None or isinstance(value, bool):
        return CORRECT_VALUES.get(value)

    return value


def get_stylish(diff, current_indent=''):
    lines = []
    for type_name, key, value in diff:
        handler = HANDLERS.get(type_name)
        indent = current_indent + INDENT
        line = handler(key, value, indent, get_stylish)
        lines.append(line)

    return '{{\n{0}\n{1}}}'.format('\n'.join(lines), current_indent)
