import os

from snipster.global_vars import SOURCE_DIR, SNIPPET_LIST_FILE
from snipster.Snippet import Snippet, SnippetError

SNIPPET_LIST = []

def source_snippets():
    if not os.path.exists(SOURCE_DIR):
        print("Initializing snipster")
        os.makedirs(SOURCE_DIR)
    walk_directories(SOURCE_DIR)
    save_snippet_list()
    print("Finished sourcing snippets.")


def walk_directories(base_path):
    all_the_files = []
    sub_directories = []
    for(_, dirnames, filename) in os.walk(base_path):
        all_the_files.extend(filename)
        sub_directories.extend(dirnames)
        break

    add_snippets_to_list(all_the_files, base_path)
    for directory in sub_directories:
        walk_directories(base_path + directory + "/")


def add_snippets_to_list(all_the_files, base_path):
    new_snippets = []
    for file in all_the_files:
        if file[0:2] == "__":
            continue
        try:
            snippet = Snippet(base_path + file)
            if int(snippet.snippet_id) == 0:
                new_snippets.append(snippet)
            else:
                SNIPPET_LIST.append(snippet)
        except SnippetError as exception:
            print("Snippet " + str(file) + " not added to list: " + str(exception))

    for snippet in new_snippets:
        new_index = len(SNIPPET_LIST)+1
        while exists_snippet(new_index):
            new_index += 1
        snippet.set_id(new_index)
        SNIPPET_LIST.append(snippet)


def exists_snippet(snippet_id):
    for snippet in SNIPPET_LIST:
        if int(snippet.snippet_id) == snippet_id:
            return True
    return False


# formatting: id;title;lang;tag1,tag2;filepath
def save_snippet_list():
    list_file = open(SOURCE_DIR + SNIPPET_LIST_FILE, "w")
    for snippet in SNIPPET_LIST:
        list_file.write(str(snippet.id) + ";")
        list_file.write(snippet.title + ";")
        list_file.write(snippet.language + ";")
        taglist = ""
        for tag in snippet.tags:
            taglist += tag + ", "
        list_file.write(taglist.rstrip(", ") + ";")
        list_file.write(snippet.path + "\n")
