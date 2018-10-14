import os

SOURCE_DIR = str(os.path.expanduser("~/.snipster/"))

SNIPPET_LIST_FILE = "__snipster__.csv"

VERSION = "1.0.3"

HELP_MESSAGE = """Snipster.

Usage:
    snipster source
    snipster list
    snipster list [-t <tag>... | -l <language>... | -k <keyword>... ]...
    snipster (-c|-e|-o) [-f] <snippet-id>
    snipster -h | --help
    snipster -v | --version

Options:
    -h, --help      Show this screen.
    -v, --version   Show version.
    -t TAG...       Filter snippet list by tag.
    -l LANGUAGE...  Filter snippet list by language.
    -k KEYWORD...   Filter snippet list by keyword.
    -c SNIPPET-ID   Copy snippet to clipboard.
    -e SNIPPET-ID   Edit snippet.
    -o SNIPPET-ID   Open snippet
    -f              Select snippet from filename instead of ID.
"""

HELP_MESSAGE_NEW = """Snipster.

Usage:
    snipster source
    snipster list [-t <tag>... | -l <language>... | -k <keyword>... ]...
    snipster (copy|edit|open) [-f] <snippet-id>
    snipster -h | --help
    snipster -v | --version

Options:
    -h, --help      Show this screen.
    -v, --version   Show version.
    -t TAG...       Filter snippet list by tag.
    -l LANGUAGE...  Filter snippet list by language.
    -k KEYWORD...   Filter snippet list by keyword.
    -f              Select snippet from filename instead of ID.
"""