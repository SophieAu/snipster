#!/usr/bin/env python3

import os
import sys

sourceDir = str(os.path.expanduser("~/.snipster"))
print(sourceDir)

def parseCLIArgs(cliArgs):
    print(cliArgs)

parseCLIArgs(sys.argv)



