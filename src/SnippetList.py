#!/usr/bin/env python3

import os
import csv
from Snippet import Snippet

snippetList = []
sourceDir = str(os.path.expanduser("~/.snipster"))
snippetListFile = "__snipster__.csv"


def lookupSnippetPath(id):
    print("looking up")
    openSnippetList()
    return findSnippet(id)

def showSnippetList(filters):
    print("show snippets")
    openSnippetList()
    print(str(filters))

def sourceSnippets():
    print("Sourcing snippets")
    walkDirectories(sourceDir)
    saveSnippetList(sourceDir)


def walkDirectories(basePath):
    allTheFiles = []
    subDirectories = []
    for(dirpath, dirnames, filename) in os.walk(basePath):
        allTheFiles.extend(filename)
        subDirectories.extend(dirnames)
        break

    for file in allTheFiles:
        if file[0:2] != "__":
            addToList(basePath + "/" + file)
    for directory in subDirectories:
        walkDirectories(basePath + "/" + directory)


# formatting: id;title;lang;tag1,tag2;filepath
def addToList(file):
    print(str(file))
    try:
        snippetList.append(Snippet(file))
    except Exception:
        print("Snippet " + str(file) + " not added to list.")

def saveSnippetList(sourceDir):
    listFile = open(sourceDir + "/" + snippetListFile, "w")
    for snippet in snippetList:
        listFile.write(snippet.id + ";")
        listFile.write(snippet.title + ";")
        listFile.write(snippet.language + ";")
        taglist = ""
        for tag in snippet.tags:
            taglist += tag + ","
        listFile.write(taglist.rstrip(",") + ";")
        listFile.write(snippet.path + "\n")

def openSnippetList():
    print("opening file")
    try:
        with open(sourceDir + "/" + snippetListFile) as snippetCSV:
            snippetListCSVFile = csv.reader(snippetCSV, delimiter= ";")
            for row in snippetListCSVFile:
                snippetList.append(row)
    except FileNotFoundError:
        print("Didn't find a snippet list file. You can create one by using the source command ('snipster source')")
        exit(1)



def findSnippet(id):
    for snippet in snippetList:
        print(str(snippet))
        if int(snippet[0]) == int(id):
            return snippet[len(snippet)-1]

    print("No snippet with id " + id + " found.")
    exit(1)
