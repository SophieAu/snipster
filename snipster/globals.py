import os

sourceDir = str(os.path.expanduser("~/.snipster/"))

snippetListFile = "__snipster__.csv"

version = "1.0.3"

help = """Snipster.

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
    -f              Select snippet from filename intead of ID.
"""
