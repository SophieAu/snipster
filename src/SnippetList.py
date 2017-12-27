#!/usr/bin/env python3

snippetList = []



def lookupSnippetPath(id):
    print("looking up")
    findSnippet(id)
    return("test.txt")

def showSnippetList(filters):
    print("show snippets")
    print(str(filters))

def sourceSnippets():
    print("Sourcing snippets")


def findSnippet(id):
    for snippet in snippetList:
        if snippet.id == id:
            return snippet.path

    print("No snippet with id " + id + " found.")
    exit(1)
