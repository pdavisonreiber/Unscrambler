# Unscrambler

A Python tool for unscrambling PDF documents, particularly useful for handling A3 booklets and rearranging pages.

## Installation

You can install the package using pip:

```bash
pip install unscrambler
```

### System Dependencies

This tool requires Ghostscript to be installed on your system for PDF optimization:

- **macOS**: Install using Homebrew:
  ```bash
  brew install ghostscript
  ```
- **Linux**: Install using your package manager:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install ghostscript
  
  # Fedora
  sudo dnf install ghostscript
  ```
- **Windows**: Download and install from [Ghostscript's official website](https://www.ghostscript.com/download/gsdnld.html)

## Usage

The unscrambler tool can be used from the command line:

```bash
unscrambler input.pdf numpages [options]
```

### Options

- `-b, --booklet`: Use this option if the original is an A3 booklet. Source PDF is expected to be in landscape with the middle pages coming first.
- `-s, --split`: Use this option if you would like the output to be split into multiple files.
- `-r, --rearrange`: Use this option to rearrange the pages.
- `-d, --doublePage`: Use this option to rearrange pages so that double pages stay together. This assumes there is a front and back cover.
- `-D, --doublePageReversed`: Use this option when unscrambling a document for which the -d option was used.
- `-y, --parseYAML`: Use when options are being parsed from a YAML file.

### Examples

1. Basic usage:
```bash
unscrambler document.pdf 4
```

2. Split a booklet:
```bash
unscrambler booklet.pdf 4 -b
```

3. Rearrange pages:
```bash
unscrambler document.pdf 4 -r
```

4. Split and rearrange:
```bash
unscrambler document.pdf 4 -s -r
```

## Development

To install the package in development mode:

```bash
pip install -e .
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 