# Generate diff

[![Actions Status](https://github.com/ilitili/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/ilitili/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a6bac6828b368a80e867/maintainability)](https://codeclimate.com/github/ilitili/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a6bac6828b368a80e867/test_coverage)](https://codeclimate.com/github/ilitili/python-project-lvl2/test_coverage)

Gendiff is a CLI utility for finding differences between configuration files.

## Features

- Suppported formats: YAML, JSON
- Report generation as plain text, structured text or JSON
- Can be used as CLI tool or external library

## Usage

### As external library

```python
from gendiff import generate_diff

diff = generate_diff(filepath1, filepath2)
```

### As CLI tool

```
> gendiff --help
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

## Installation

```bash
pip install --user --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ ilitili
```

[![asciicast](https://asciinema.org/a/5dvZj3cRAsUWtwg9cy3xghYIG.svg)](https://asciinema.org/a/5dvZj3cRAsUWtwg9cy3xghYIG)
