import os
import sys
import subprocess

from snipster.global_vars import SOURCE_DIR, VERSION, HELP_MESSAGE
from snipster.snippet import Snippet, SnippetError
from snipster.snippet_list import show_snippet_list, lookup_snippet_path
from snipster.sourcer import source_snippets

def main():
    parse_cli_args(sys.argv[1:])
    exit(0)


def parse_cli_args(cli_args):
    if not cli_args or cli_args[0] == "-h" or cli_args[0] == "--HELP_MESSAGE":
        print(HELP_MESSAGE)
        return
    if cli_args[0] == "-v" or cli_args[0] == "--VERSION":
        print(VERSION)
        return

    if cli_args[0] == "source":
        source_snippets()
        return
    elif cli_args[0] == "list":
        show_snippet_list(cli_args[1:])
        return

    else:
        last_arg = cli_args[len(cli_args)-1]
        if (len(cli_args[0]) == 3 and cli_args[0][2] == "f") or (len(cli_args) == 3 and cli_args[1] == "-f"):
            snippet_file_path = SOURCE_DIR + last_arg
        else:
            try:
                int(last_arg)
            except ValueError:
                print(HELP_MESSAGE)
                return

            snippet_file_path = lookup_snippet_path(last_arg)

    if cli_args[0][:2] == "-o":
        try:
            Snippet(snippet_file_path).display()
        except SnippetError as exception:
            print(str(exception))

    elif cli_args[0][:2] == "-c":
        try:
            Snippet(snippet_file_path).copy_to_clipboard()
        except SnippetError as exception:
            print(str(exception))

    elif cli_args[0][:2] == "-e":
        open_in_editor(snippet_file_path)


def open_in_editor(snippet_file_path):
    editor = os.environ.get('VISUAL') or os.environ.get('EDITOR') or False

    # assert that the editor is set
    if not editor:
        print("Please set VISUAL or EDITOR in your bashrc to be able to create/edit snippets.")
        exit(1)

    try:
        subprocess.run(editor.split(" ") + [snippet_file_path])
    except OSError:
        print('Could not launch ' + editor)
        exit(1)
