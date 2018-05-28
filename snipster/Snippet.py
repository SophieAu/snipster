from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.terminal256 import Terminal256Formatter
import pyperclip

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
            raise FileNotFoundError("File " + path + " not found.")

        self.path = path


    def parse(self, file):
        # validate file formatting
        if file.readline() != "---\n":
            raise Exception("File not a valid snippet")
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
            self.id = int(values)
        elif key == "tags":
            self.tags = [tag.lstrip(" ").rstrip(" ") for tag in values.split(",")]
        elif key == "title":
            self.title = values.lstrip("\"").rstrip("\"")
        elif key == "lang":
            self.language = values

    def setId(self, id):
        with open(self.path, "r+") as file:
            file.readline()
            oldFile = file.read()
            file.seek(0,0)
            file.write("---\nid: " + str(id) + "\n" + oldFile)
        self.id = id

    def display(self):
        lexer = get_lexer_by_name(self.codeLanguage, stripall=True)
        formatter = Terminal256Formatter()
        code = highlight(self.code, lexer, formatter)
        print("#" + str(self.id) + ": \033[1m" + self.title + "\033[0m\n")
        print(self.description + "\n")
        print(code)


    def copyToClipboard(self):
        pyperclip.copy(self.code)
        print("Copied snippet #" + str(self.id) + " to the clipboard.")


