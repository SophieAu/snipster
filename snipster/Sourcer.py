import os

from snipster.globalVars import source_dir, snippet_list_file
from snipster.Snippet import Snippet

snippet_list = []

def source_snippets():
    if not os.path.exists(source_dir):
        print("Initializing snipster")
        os.makedirs(source_dir)
    walk_directories(source_dir)
    save_snippet_list(source_dir)
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
            if int(snippet.id) == 0:
                new_snippets.append(snippet)
            else:
                snippet_list.append(snippet)
        except Exception as e:
            print("Snippet " + str(file) + " not added to list: " + str(e))

    for snippet in new_snippets:
        new_index = len(snippet_list)+1
        while existsSnippet(new_index):
            new_index += 1
        snippet.setId(new_index)
        snippet_list.append(snippet)


def existsSnippet(id):
    for snippet in snippet_list:
        if int(snippet.id) == id:
            return True
    return False


# formatting: id;title;lang;tag1,tag2;filepath
def save_snippet_list(source_dir):
    list_file = open(source_dir + snippet_list_file, "w")
    for snippet in snippet_list:
        list_file.write(str(snippet.id) + ";")
        list_file.write(snippet.title + ";")
        list_file.write(snippet.language + ";")
        taglist = ""
        for tag in snippet.tags:
            taglist += tag + ", "
        list_file.write(taglist.rstrip(", ") + ";")
        list_file.write(snippet.path + "\n")
