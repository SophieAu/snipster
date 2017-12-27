#!/usr/bin/env python3

import os

snippetList = ""
sourceDir = str(os.path.expanduser("~/.snipster"))
snippetListFile = "__snipster__.csv"


def lookupSnippetPath(id):
    print("looking up")
    openSnippetList()
    findSnippet(id)
    return("test.txt")

def showSnippetList(filters):
    print("show snippets")
    print(str(filters))

def sourceSnippets():
    print("Sourcing snippets")

def openSnippetList():
    print("opening file")
    try:
        with open(sourceDir + "/" + snippetListFile) as snippetCSV:
            snippetList = csv.reader(snippetCSV)
    except FileNotFoundError:
        print("Didn't find a snippet list file. You can create one by using the source command ('snipster source')")
        exit(1)



def findSnippet(id):
    for snippet in snippetList:
        if snippet[0] == id:
            return snippet[len(snippet)-1]

    print("No snippet with id " + id + " found.")
    exit(1)
