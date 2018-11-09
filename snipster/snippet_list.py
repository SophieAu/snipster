import csv
from tabulate import tabulate

from snipster.global_vars import SOURCE_DIR, SNIPPET_LIST_FILE
from snipster.snippet import Snippet

SNIPPET_LIST = []
TAGS = []
KEYWORDS = []
LANGUAGES = []
FILTERED_SNIPPET_LIST = []
TAG_HITS = []
KEYWORD_HITS = []
LANGUAGE_HITS = []

def lookup_snippet_path(snippet_id):
    open_snippet_list()
    return find_snippet(snippet_id)


def show_snippet_list(filters):
    global FILTERED_SNIPPET_LIST
    open_snippet_list()
    if filters != []:
        set_up_filters(filters)
        filter_snippets()
    else:
        FILTERED_SNIPPET_LIST = SNIPPET_LIST
    print_snippets()


def filter_snippets():
    for snippet in SNIPPET_LIST:
        if TAGS:
            filter_by_tag(snippet)
        if KEYWORDS:
            filter_by_keyword(snippet)
        if LANGUAGES:
            filter_by_language(snippet)
    union_filter_hits()


def union_filter_hits():
    temp_list = []
    for snippet in TAG_HITS:
        if (not KEYWORDS or snippet in KEYWORD_HITS) and (not LANGUAGES or snippet in LANGUAGE_HITS):
            temp_list.append(snippet)
    for snippet in KEYWORD_HITS:
        if (not TAGS or snippet in TAG_HITS) and (not KEYWORDS or snippet in KEYWORD_HITS):
            temp_list.append(snippet)

    seen = []
    for snippet in temp_list:
        if snippet not in seen:
            FILTERED_SNIPPET_LIST.append(snippet)
            seen.append(snippet)


def filter_by_tag(snippet):
    for tag in TAGS:
        if tag.lower() in snippet[3].lower():
            TAG_HITS.append(snippet)
            return


def filter_by_keyword(snippet):
    for keyword in KEYWORDS:
        if keyword.lower() in snippet[1].lower():
            KEYWORD_HITS.append(snippet)
            return


def filter_by_language(snippet):
    for language in LANGUAGES:
        if language.lower() in snippet[2].lower():
            LANGUAGE_HITS.append(snippet)
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
            TAGS.append(value)
        if filter_type == "keywords":
            KEYWORDS.append(value)
        if filter_type == "language":
            LANGUAGES.append(value)


def print_snippets():
    headers = ["ID", "Title", "Language", "Tags", "Filename"]
    table = []
    if not FILTERED_SNIPPET_LIST:
        print("No matches.")
        return
    if len(FILTERED_SNIPPET_LIST) == 1:
        Snippet(FILTERED_SNIPPET_LIST[0][4]).display()
        return
    for snippet in FILTERED_SNIPPET_LIST:
        file_path_index = len(snippet)-1
        snippet[file_path_index] = snippet[file_path_index][len(SOURCE_DIR):]
        table.append(snippet)
    print(tabulate(FILTERED_SNIPPET_LIST, headers=headers, tablefmt="pipe"))


def open_snippet_list():
    try:
        with open(SOURCE_DIR + SNIPPET_LIST_FILE) as snippet_csv:
            snippet_list_csv_file = csv.reader(snippet_csv, delimiter=";")
            for row in snippet_list_csv_file:
                SNIPPET_LIST.append(row)
    except FileNotFoundError:
        print("Didn't find a snippet list file. You can create one by using the source command ('snipster source')")
        exit(1)


def find_snippet(snippet_id):
    for snippet in SNIPPET_LIST:
        if int(snippet[0]) == int(snippet_id):
            return snippet[len(snippet)-1]
    print("No snippet with id " + str(snippet_id) + " found.")
    exit(1)
