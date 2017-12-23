#!/usr/bin/env python3

import os
import sys

sourceDir = str(os.path.expanduser("~/.snipster"))
print(sourceDir)

def parseCLIArgs(cliArgs):
    del cliArgs[0] # deletes the snipster command
    print(cliArgs)

    # open file specified in the now 1st argument
    try:
        with open(sourceDir + "/" + cliArgs[0]) as snippet:
            print(snippet.readline()) # print first line of the file
    except FileNotFoundError:
        print("File not found")


parseCLIArgs(sys.argv)



