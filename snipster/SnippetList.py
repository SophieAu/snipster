import os
import csv

from snipster.globalVars import sourceDir, snippetListFile
from snipster.Snippet import Snippet
from tabulate import tabulate

snippetList = []
tags = []
keywords = []
languages = []
filteredSnippetList = []
tagHits = []
keywordHits = []
languageHits = []

def lookupSnippetPath(id):
    openSnippetList()
    return findSnippet(id)

def showSnippetList(filters):
    global filteredSnippetList
    openSnippetList()
    if filters != []:
        setUpFilters(filters)
        filterSnippets()
    else:
        filteredSnippetList = snippetList
    printSnippets()

def filterSnippets():
    for snippet in snippetList:
        if len(tags) != 0:
            filterByTag(snippet)
        if len(keywords) !=0:
            filterByKeyword(snippet)
        if len(languages) != 0:
            filterByLanguage(snippet)
    unionFilterHits()

def unionFilterHits():
    tempList = []
    for snippet in tagHits:
        if (len(keywords) == 0 or snippet in keywordHits) and (len(languages) == 0 or snippet in languageHits):
            tempList.append(snippet)
    for snippet in keywordHits:
        if (len(tags) == 0 or snippet in tagHits) and (len(languages) == 0 or snippet in languageHits):
            tempList.append(snippet)
    for snippet in languageHits:
        if (len(tags) == 0 or snippet in tagHits) and (len(keywords) == 0 or snippet in keywordHits):
            tempList.append(snippet)

    seen = []
    for snippet in tempList:
        if snippet not in seen:
            filteredSnippetList.append(snippet)
            seen.append(snippet)

def filterByTag(snippet):
    for tag in tags:
        if tag.lower() in snippet[3].lower():
            tagHits.append(snippet)
            return

def filterByKeyword(snippet):
    for keyword in keywords:
        if keyword.lower() in snippet[1].lower():
            keywordHits.append(snippet)
            return

def filterByLanguage(snippet):
    for language in languages:
        if language.lower() in snippet[2].lower():
            languageHits.append(snippet)
            return


def setUpFilters(filters):
    for value in filters:
        if value == "-t":
            filterType = "tags"
            continue
        elif value == "-k":
            filterType = "keywords"
            continue
        elif value == "-l":
            filterType = "language"
            continue

        if filterType == "tags":
            tags.append(value)
        if filterType == "keywords":
            keywords.append(value)
        if filterType == "language":
            languages.append(value)


def printSnippets():
    headers = ["ID", "Title", "Language", "Tags", "Filename"]
    table = []
    if len(filteredSnippetList) == 0:
        print("No matches.")
        return
    if len(filteredSnippetList) == 1:
        Snippet(filteredSnippetList[0][4]).display()
        return
    for snippet in filteredSnippetList:
        filePathIndex = len(snippet)-1
        snippet[filePathIndex] = snippet[filePathIndex][len(sourceDir):]
        table.append(snippet)
    print(tabulate(filteredSnippetList, headers=headers, tablefmt="pipe"))


def openSnippetList():
    try:
        with open(sourceDir + snippetListFile) as snippetCSV:
            snippetListCSVFile = csv.reader(snippetCSV, delimiter= ";")
            for row in snippetListCSVFile:
                snippetList.append(row)
    except FileNotFoundError:
        print("Didn't find a snippet list file. You can create one by using the source command ('snipster source')")
        exit(1)

def findSnippet(id):
    for snippet in snippetList:
        if int(snippet[0]) == int(id):
            return snippet[len(snippet)-1]
    print("No snippet with id " + str(id) + " found.")
    exit(1)

