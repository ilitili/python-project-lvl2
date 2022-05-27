import json
from types import MappingProxyType

import yaml

LOADERS = MappingProxyType({
    'json': json.loads,
    'yml': yaml.safe_load,
    'yaml': yaml.safe_load,
})


def get_loader(ext):
    if ext in LOADERS:
        return LOADERS.get(ext)
    raise ValueError
