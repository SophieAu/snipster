import os
import sys
import subprocess

from snipster.globalVars import sourceDir, snippetListFile, version, help
from snipster.Snippet import Snippet
from snipster.SnippetList import showSnippetList, lookupSnippetPath
from snipster.Sourcer import sourceSnippets

def main():
    parseCLIArgs(sys.argv[1:])
    exit(0)

def parseCLIArgs(cliArgs):
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
            snippetFilePath = sourceDir + lastArg
        else:
            try:
                int(lastArg)
            except ValueError:
                print(help)
                return

            snippetFilePath = lookupSnippetPath(lastArg)

    if cliArgs[0][:2] == "-o":
        try:
            Snippet(snippetFilePath).display()
        except Exception as e:
            print(str(e))

    elif cliArgs[0][:2] == "-c":
        try:
            Snippet(snippetFilePath).copyToClipboard()
        except Exception as e:
            print(str(e))

    elif cliArgs[0][:2] == "-e":
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
