#!/usr/bin/env python3

class Snippet:
    path = ""

    def __init__(self, file, path):
        self.parse(file)
        self.path = path
        print(self.path)

    def parse(self, file):
        if file.readline() != "---\n":
            print("File not a valid snippet")
            exit(1)
        print(file.readline())
        print("Hello")
