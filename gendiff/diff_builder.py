from operator import itemgetter

from pydash import find

ADDED = 'ADDED'
REMOVED = 'REMOVED'
CHANGED = 'CHANGED'
UNCHANGED = 'UNCHANGED'
EMBEDDED = 'EMBEDDED'

TYPE = 'type'
CHECK = 'check'
PROCESS = 'process'

TYPES = (
    {
        TYPE: EMBEDDED,
        CHECK: lambda dict1, dict2, key:
            isinstance(dict1.get(key), dict) and isinstance(dict2.get(key), dict),
        PROCESS: lambda first_value, second_value, func: func(first_value, second_value),
    },
    {
        TYPE: UNCHANGED,
        CHECK: lambda dict1, dict2, key:
            key in dict1 and key in dict2 and dict1[key] == dict2[key],
        PROCESS: lambda first_value, _, __: first_value,
    },
    {
        TYPE: CHANGED,
        CHECK: lambda dict1, dict2, key:
            key in dict1 and key in dict2 and dict1[key] != dict2[key],
        PROCESS: lambda first_value, second_value, _: (first_value, second_value),
    },
    {
        TYPE: REMOVED,
        CHECK: lambda dict1, dict2, key: key in dict1 and key not in dict2,
        PROCESS: lambda first_value, _, __: first_value,
    },
    {
        TYPE: ADDED,
        CHECK: lambda dict1, dict2, key: key not in dict1 and key in dict2,
        PROCESS: lambda _, second_value, __: second_value,
    },
)


def build_diff(dict1, dict2):
    keys = sorted(set(dict1) | set(dict2))

    diff = []

    for key in keys:
        first_value = dict1.get(key)
        second_value = dict2.get(key)

        current_type = find(TYPES, lambda item: item[CHECK](dict1, dict2, key))
        type_name, process = itemgetter(TYPE, PROCESS)(current_type)

        value = process(first_value, second_value, build_diff)
        diff.append((type_name, key, value))

    return diff
