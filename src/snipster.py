#!/usr/bin/env python3

import os
import sys
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import Terminal256Formatter

from Snippet import Snippet


sourceDir = str(os.path.expanduser("~/.snipster"))
version = "0.1.0"
help = """Snipster.
Usage:

Other Stuff:"""

def parseCLIArgs(cliArgs):
    del cliArgs[0] # deletes the snipster command
    # open file specified in the now 1st argument
    filePath = sourceDir + "/" + cliArgs[0]
    try:
        with open(filePath) as snippetFile:
            snippet = Snippet(snippetFile, filePath)
    except FileNotFoundError:
        print("File not found")
        exit(1)

def displaySnippet(snippet):
    lexer = get_lexer_by_name(snippet.codeLanguage, stripall=True)
    formatter = Terminal256Formatter()
    code = highlight(snippet.code, lexer, formatter)
    print("#" + snippet.id + ": \033[1m" + snippet.title + "\033[0m\n")
    print(snippet.description + "\n")
    print(code)

    if len(cliArgs) == 0 or cliArgs[0] == "-h" or cliArgs[0] == "--help":
        print(help)
        return
    if cliArgs[0] == "-v" or cliArgs[0] == "--version":
        print(version)
        return

    if cliArgs[0] == "source":
        print("source snippets")
        return
    elif cliArgs[0] == "list":
        print("Show snippets")
        return

    else:
        lastArg = cliArgs[len(cliArgs)-1]
        if (len(cliArgs[0]) == 3 and cliArgs[0][2] == "f") or (len(cliArgs) == 3 and cliArgs[1] == "-f"):
            print("File from path")
            snippetFilePath = lastArg
        else:
            try:
                int(lastArg)
            except ValueError:
                print(help)
                return

            print(lastArg)
            print("File from id")
            snippetFilePath = lookupSnippetPath(lastArg)
    snippetFilePath = sourceDir + "/" + snippetFilePath

    if cliArgs[0][:2] == "-o":
        print("show snippet")
    elif cliArgs[0][:2] == "-c":
        print("copy snippet")
    elif cliArgs[0][:2] == "-e":
        print("edit snippet")


def lookupSnippetPath(id):
    print("looking up")
    return("test.txt")

parseCLIArgs(sys.argv)

