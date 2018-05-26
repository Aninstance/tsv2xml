import os
from contextlib import contextmanager
from xml.sax.saxutils import escape
import click


class InputFile:

    def __init__(self, inpt: str):
        inpt = inpt.split(':')
        self.filename = inpt[0]
        if len(inpt) == 2:
            self.nodename = inpt[1]
        else:
            filename_w_ext = os.path.basename(inpt[0])
            nodename, fileext = os.path.splitext(filename_w_ext)
            self.nodename = nodename


@contextmanager
def node(node_name: str, depth: int, wrapping=False):
    print(' ' * depth * 4, end='')
    print('<{}>'.format(node_name), end='')
    if not wrapping:
        print()
    yield
    if not wrapping:
        print(' ' * depth * 4, end='')
    print('</{}>'.format(node_name))


@click.command()
@click.option('--limit', '-l', type=int, help='Number of lines included of each .tsv/.tab file.')
@click.argument('fileargs', nargs=-1, metavar='FILEARGS[:NODENAME]')
def cli(fileargs, limit):
    print('<?xml version="1.0" encoding="UTF-8"?>')
    with node('root', 0):
        for filearg in fileargs:
            inptfile = InputFile(filearg)
            with node(inptfile.nodename, 1):
                with open(inptfile.filename) as file:
                    headers = file.readline().split('\t')
                    if limit:
                        records = zip(range(limit), file)
                    else:
                        records = file
                    for _, record in records:
                        with node('record', 2):
                            for idx, col in enumerate(record.split('\t')):
                                with node(headers[idx].strip(), 3, wrapping=True):
                                    print(escape(col.strip()), end='')
