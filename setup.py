from setuptools import setup

setup(
    name='tsv2xml',
    version='1.0.0-SNAPSHOT',
    py_modules=['tsv2xml'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        tsv2xml=tsv2xml.tsv2xml:cli
    ''',
)