#!/usr/bin/env python3

class Snippet:
    path = ""
    id = 0
    tags = []
    language = ""
    title = ""
    description = ""
    codeLanguage = ""
    code = ""

    def __init__(self, path):
        try:
            with open(path) as file:
                self.parse(file)
        except FileNotFoundError:
            print("File not Found")
            exit(1)

        self.path = path


    def parse(self, file):
        # validate file formatting
        if file.readline() != "---\n":
            print("File not a valid snippet")
            exit(1)
        currentLine = file.readline()

        # parse frontmatter
        while currentLine != "---\n":
            key,value = currentLine.split(":",1)
            self.assignKeyValues(key, value.lstrip(" ").rstrip("\n"))
            currentLine = file.readline()
        currentLine = file.readline()

        # parse description
        while currentLine[:3] != "```":
            self.description += currentLine
            currentLine = file.readline()
        self.description = self.description.lstrip("\n").rstrip("\n")

        # parse actual language of the file (for syntax highlighting)
        self.codeLanguage = currentLine.lstrip("```").rstrip("\n")
        currentLine = file.readline()

        # parse actual file (the code)
        while currentLine != "```\n":
            self.code += currentLine
            currentLine = file.readline()
        self.code = self.code.rstrip("\n")


    def assignKeyValues(self, key, values):
        if key == "id":
            self.id = values
        elif key == "tags":
            self.tags = [tag.lstrip(" ").rstrip(" ") for tag in values.split(",")]
        elif key == "title":
            self.title = values.lstrip("\"").rstrip("\"")
        elif key == "lang":
            self.language = values

