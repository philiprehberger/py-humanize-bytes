# philiprehberger-humanize-bytes

[![Tests](https://github.com/philiprehberger/py-humanize-bytes/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-humanize-bytes/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-humanize-bytes.svg)](https://pypi.org/project/philiprehberger-humanize-bytes/)
[![Last updated](https://img.shields.io/github/last-commit/philiprehberger/py-humanize-bytes)](https://github.com/philiprehberger/py-humanize-bytes/commits/main)

Convert byte counts to human-readable strings and back, with formatting options.

## Installation

```bash
pip install philiprehberger-humanize-bytes
```

## Usage

```python
from philiprehberger_humanize_bytes import format_bytes, parse_bytes
```

### Formatting bytes

```python
format_bytes(1536)          # "1.5 KiB"
format_bytes(1048576)       # "1 MiB"
format_bytes(0)             # "0 B"
format_bytes(-1536)         # "-1.5 KiB"
```

### SI units (base 1000)

```python
format_bytes(1500, si=True)           # "1.5 KB"
format_bytes(1000000, si=True)        # "1 MB"
format_bytes(2500000000, si=True)     # "2.5 GB"
```

### Custom precision

```python
format_bytes(123456789, precision=2)  # "117.74 MiB"
format_bytes(123456789, precision=0)  # "118 MiB"
```

### Parsing byte strings

```python
parse_bytes("1.5 GB")    # 1500000000
parse_bytes("1.5 GiB")   # 1610612736
parse_bytes("500 KB")     # 500000
parse_bytes("10M")        # 10000000
parse_bytes("1024")       # 1024
```

## API

| Function | Description |
|----------|-------------|
| `format_bytes(n, *, si=False, precision=1)` | Format byte count to human-readable string. Binary (KiB/MiB/GiB) by default, SI (KB/MB/GB) with `si=True`. |
| `parse_bytes(s)` | Parse a human-readable byte string to an integer. Supports binary, SI, and shorthand units. Case-insensitive. |

## Development

```bash
pip install -e .
python -m pytest tests/ -v
```

## Support

If you find this project useful:

⭐ [Star the repo](https://github.com/philiprehberger/py-humanize-bytes)

🐛 [Report issues](https://github.com/philiprehberger/py-humanize-bytes/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

💡 [Suggest features](https://github.com/philiprehberger/py-humanize-bytes/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)

❤️ [Sponsor development](https://github.com/sponsors/philiprehberger)

🌐 [All Open Source Projects](https://philiprehberger.com/open-source-packages)

💻 [GitHub Profile](https://github.com/philiprehberger)

🔗 [LinkedIn Profile](https://www.linkedin.com/in/philiprehberger)

## License

[MIT](LICENSE)
