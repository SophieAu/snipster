import os

from snipster.globalVars import sourceDir, snippetListFile
from snipster.Snippet import Snippet

snippetList = []

def sourceSnippets():
    if not os.path.exists(sourceDir):
        print("Initializing snipster")
        os.makedirs(sourceDir)
    walkDirectories(sourceDir)
    saveSnippetList(sourceDir)
    print("Finished sourcing snippets.")


def walkDirectories(basePath):
    allTheFiles = []
    subDirectories = []
    for(_, dirnames, filename) in os.walk(basePath):
        allTheFiles.extend(filename)
        subDirectories.extend(dirnames)
        break

    addSnippetsToList(allTheFiles, basePath)
    for directory in subDirectories:
        walkDirectories(basePath + directory + "/")


def addSnippetsToList(allTheFiles, basePath):
    newSnippets = []
    for file in allTheFiles:
        if file[0:2] == "__":
            continue
        try:
            snippet = Snippet(basePath + file)
            if int(snippet.id) == 0:
                newSnippets.append(snippet)
            else:
                snippetList.append(snippet)
        except Exception as e:
            print("Snippet " + str(file) + " not added to list: " + str(e))

    for snippet in newSnippets:
        newIndex = len(snippetList)+1
        while existsSnippet(newIndex):
            newIndex += 1
        snippet.setId(newIndex)
        snippetList.append(snippet)


def existsSnippet(id):
    for snippet in snippetList:
        if int(snippet.id) == id:
            return True
    return False


# formatting: id;title;lang;tag1,tag2;filepath
def saveSnippetList(sourceDir):
    listFile = open(sourceDir + snippetListFile, "w")
    for snippet in snippetList:
        listFile.write(str(snippet.id) + ";")
        listFile.write(snippet.title + ";")
        listFile.write(snippet.language + ";")
        taglist = ""
        for tag in snippet.tags:
            taglist += tag + ", "
        listFile.write(taglist.rstrip(", ") + ";")
        listFile.write(snippet.path + "\n")

