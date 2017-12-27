#!/usr/bin/env python3

import os
import sys
import subprocess

from Snippet import Snippet
from SnippetList import *


sourceDir = str(os.path.expanduser("~/.snipster"))
version = "0.1.0"
help = """Snipster.
Usage:

Other Stuff:"""

def parseCLIArgs(cliArgs):
    del cliArgs[0] # deletes the snipster command

    if len(cliArgs) == 0 or cliArgs[0] == "-h" or cliArgs[0] == "--help":
        print(help)
        return
    if cliArgs[0] == "-v" or cliArgs[0] == "--version":
        print(version)
        return

    if cliArgs[0] == "source":
        sourceSnippets()
        return
    elif cliArgs[0] == "list":
        showSnippetList(cliArgs[1:])
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
        try:
            Snippet(snippetFilePath).display()
        except Exception as e:
            print(str(e))

    elif cliArgs[0][:2] == "-c":
        print("copy snippet")
        try:
            Snippet(snippetFilePath).copyToClipboard()
        except Exception as e:
            print(str(e))

    elif cliArgs[0][:2] == "-e":
        print("edit snippet")
        openInEditor(snippetFilePath)


def openInEditor(snippetFilePath):
    editor = os.environ.get('VISUAL') or os.environ.get('EDITOR') or False

    # assert that the editor is set
    if editor == False:
        print("Please set VISUAL or EDITOR in your bashrc to be able to create/edit snippets.")
        exit(1)

    try:
        subprocess.run(editor.split(" ") + [snippetFilePath])
    except OSError:
        print('Could not launch ' + editor)
        exit(1)



parseCLIArgs(sys.argv)

