#!/usr/bin/env python3

import os
import sys

from Snippet import Snippet

sourceDir = str(os.path.expanduser("~/.snipster"))
print(sourceDir)

def parseCLIArgs(cliArgs):
    del cliArgs[0] # deletes the snipster command
    print(cliArgs)

    # open file specified in the now 1st argument
    filePath = sourceDir + "/" + cliArgs[0]
    try:
        with open(filePath) as snippetFile:
            snippet = Snippet(snippetFile, filePath)
    except FileNotFoundError:
        print("File not found")


parseCLIArgs(sys.argv)



