import os
import csv

from snipster.globalVars import source_dir, snippet_list_file
from snipster.Snippet import Snippet
from tabulate import tabulate

snippet_list = []
tags = []
keywords = []
languages = []
filtered_snippet_list = []
tag_hits = []
keyword_hits = []
language_hits = []

def lookup_snippet_path(id):
    open_snippet_list()
    return find_snippet(id)

def show_snippet_list(filters):
    global filtered_snippet_list
    open_snippet_list()
    if filters != []:
        set_up_filters(filters)
        filter_snippets()
    else:
        filtered_snippet_list = snippet_list
    print_snippets()

def filter_snippets():
    for snippet in snippet_list:
        if len(tags) != 0:
            filter_by_tag(snippet)
        if len(keywords) !=0:
            filter_by_keyword(snippet)
        if len(languages) != 0:
            filter_by_language(snippet)
    union_filter_hits()

def union_filter_hits():
    temp_list = []
    for snippet in tag_hits:
        if (len(keywords) == 0 or snippet in keyword_hits) and (len(languages) == 0 or snippet in language_hits):
            temp_list.append(snippet)
    for snippet in keyword_hits:
        if (len(tags) == 0 or snippet in tag_hits) and (len(languages) == 0 or snippet in language_hits):
            temp_list.append(snippet)
    for snippet in language_hits:
        if (len(tags) == 0 or snippet in tag_hits) and (len(keywords) == 0 or snippet in keyword_hits):
            temp_list.append(snippet)

    seen = []
    for snippet in temp_list:
        if snippet not in seen:
            filtered_snippet_list.append(snippet)
            seen.append(snippet)

def filter_by_tag(snippet):
    for tag in tags:
        if tag.lower() in snippet[3].lower():
            tag_hits.append(snippet)
            return

def filter_by_keyword(snippet):
    for keyword in keywords:
        if keyword.lower() in snippet[1].lower():
            keyword_hits.append(snippet)
            return

def filter_by_language(snippet):
    for language in languages:
        if language.lower() in snippet[2].lower():
            language_hits.append(snippet)
            return


def set_up_filters(filters):
    for value in filters:
        if value == "-t":
            filter_type = "tags"
            continue
        elif value == "-k":
            filter_type = "keywords"
            continue
        elif value == "-l":
            filter_type = "language"
            continue

        if filter_type == "tags":
            tags.append(value)
        if filter_type == "keywords":
            keywords.append(value)
        if filter_type == "language":
            languages.append(value)


def print_snippets():
    headers = ["ID", "Title", "Language", "Tags", "Filename"]
    table = []
    if len(filtered_snippet_list) == 0:
        print("No matches.")
        return
    if len(filtered_snippet_list) == 1:
        Snippet(filtered_snippet_list[0][4]).display()
        return
    for snippet in filtered_snippet_list:
        file_path_index = len(snippet)-1
        snippet[file_path_index] = snippet[file_path_index][len(source_dir):]
        table.append(snippet)
    print(tabulate(filtered_snippet_list, headers=headers, tablefmt="pipe"))


def open_snippet_list():
    try:
        with open(source_dir + snippet_list_file) as snippet_csv:
            snippet_list_csv_file = csv.reader(snippet_csv, delimiter= ";")
            for row in snippet_list_csv_file:
                snippet_list.append(row)
    except FileNotFoundError:
        print("Didn't find a snippet list file. You can create one by using the source command ('snipster source')")
        exit(1)

def find_snippet(id):
    for snippet in snippet_list:
        if int(snippet[0]) == int(id):
            return snippet[len(snippet)-1]
    print("No snippet with id " + str(id) + " found.")
    exit(1)
