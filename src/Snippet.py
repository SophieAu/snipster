#!/usr/bin/env python3

class Snippet:
    path = ""
    id = 0
    tags = []
    lang = ""
    title = ""
    description = ""
    code = ""

    def __init__(self, file, path):
        self.parse(file)
        self.path = path
        print(self.path)
        print(self.id)
        print(str(self.tags))
        print(self.lang)
        print(self.title)
        print(self.description)
        print(self.code)

    def parse(self, file):
        if file.readline() != "---\n":
            print("File not a valid snippet")
            exit(1)
        print(file.readline())
        print("Hello")
