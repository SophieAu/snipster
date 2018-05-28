from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name         = 'snipster-py',
    version      = '1.0.3',
    author       = 'Sophie Au',
    author_email = 'some.person@web.de',
    license      = 'MIT',
    description  = 'A simple command line snippet manager',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords     = ['snippet', 'snippets-manager', 'command-line-tool'],
    url          = 'https://github.com/sophieau/snipster',

    packages     = ['snipster'],
    zip_safe     = False,
    entry_points = {
        'console_scripts': ['snipster=snipster.__main__:main'],
    },
    python_requires  = '>=3.6',
    install_requires = [
        'Pygments >= 2.2.0',
        'pyperclip >= 1.6.0',
        'tabulate >= 0.8.2',
    ]
)
