# tsv2xml

Command line tool to map tab separated values files into xml output.

```bash
Usage: tsv2xml [OPTIONS] FILEARGS[:NODENAME]

Options:
  -l, --limit INTEGER  Number of lines included of each .tsv/.tab file.
  -s, --skip INTEGER   Number of lines to skip before starting, for each
                       .tsv/.tab file.
  --help               Show this message and exit.
```

First line of each file is expected to be a header, 
the tab separated names of columns.

## Dependencies

* Python 3.x
* Pip

## Installation

1. Clone project with git:
    ```bash
    git clone https://github.com/mglezsosa/tsv2xml.git
    ```

2. Install:
    ```bash
    cd tsv2xml && make install
    ```
    
    or
    
    ```bash
    cd tsv2xml && pip install -e .
    ```

## Example

```bash
tsv2xml proteins.tsv organisms.tsv formed_by.tsv:formedby date_of.tsv:dateof --limit=20 > myxmlfile.xml
```
