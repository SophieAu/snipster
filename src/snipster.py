#!/usr/bin/env python3

import os
import sys
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import Terminal256Formatter

from Snippet import Snippet


sourceDir = str(os.path.expanduser("~/.snipster"))

def parseCLIArgs(cliArgs):
    del cliArgs[0] # deletes the snipster command
    # DEBUG: print("CLI Arguments: \"" + "\" \"".join(cliArgs) + "\"\n\n\n")

    # open file specified in the now 1st argument
    filePath = sourceDir + "/" + cliArgs[0]
    try:
        with open(filePath) as snippetFile:
            snippet = Snippet(snippetFile, filePath)
    except FileNotFoundError:
        print("File not found")
        exit(1)

    displaySnippet(snippet)


def displaySnippet(snippet):
    lexer = get_lexer_by_name(snippet.codeLanguage, stripall=True)
    formatter = Terminal256Formatter()
    code = highlight(snippet.code, lexer, formatter)
    print("\033[1m" + snippet.title + "\033[0m\n")
    print(snippet.description + "\n")
    print(code)




parseCLIArgs(sys.argv)



