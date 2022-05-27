import json


def transform_diff(diff):
    result = {}
    for item in diff:
        type_name, key, value = item
        result[key] = {
            'type': type_name,
            'value': transform_diff(value) if isinstance(value, list) else value,
        }
    return result


def get_json(diff):
    return json.dumps(transform_diff(diff), indent=4)
