from distutils.core import setup
from setuptools import setup

setup(
    name         = 'snipster-py',
    version      = '1.0.3',
    author       = 'Sophie Au',
    author_email = 'some.person@web.de',
    license      = 'MIT',
    description  = 'A simple command line snippet manager',
    keywords     = ['snippet', 'snippets-manager', 'command-line-tool'],
    url          = 'https://github.com/sophieau/snipster',

    packages     = ['snipster'],
	entry_points={
		'console_scripts': [
			'snipster = snipster.snipster:main'
		]
	},
    python_requires  = '>=3.6',
    install_requires = [
        'Pygments >= 2.2.0',
        'pyperclip >= 1.6.0',
        'tabulate >= 0.8.2',
    ]
)
