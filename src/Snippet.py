#!/usr/bin/env python3

class Snippet:
    path = ""

    def __init__(self, file, path):
        self.parse(file)
        self.path = path
        print(self.path)

    def parse(self, file):
        print(file.readline())
        print("Hello")
