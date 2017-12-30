from distutils.core import setup
from setuptools import setup

setup(
    name         = 'snipster',
    version      = '1.0',
    author       = 'Sophie Au',
    author_email = 'some.person@web.de',
    license      = 'MIT',
    description  = 'A simple command line snippet manager',
    keywords     = ['snippet', 'snippets-manager', 'command-line-tool'],
    url          = 'https://github.com/sophieau/snipster',

    download_url = 'https://github.com/sophieau/snipster/archive/v1.0.tar.gz', # I'll explain this in a second
    packages     = ['src'], # this must be the same as the name above
    classifiers  = [],

    python_requires  = '>=3.6',
    install_requires = [
        'pygment >= 2.2.0',
        'pyperclip >= 1.6.0',
        'tabulate >= 0.8.2',
    ]
)
