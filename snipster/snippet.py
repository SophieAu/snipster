from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.terminal256 import Terminal256Formatter
import pyperclip

class SnippetError(Exception):
    pass

class Snippet:
    path = ""
    snippet_id = 0
    tags = []
    language = ""
    title = ""
    description = ""
    code_language = ""
    code = ""

    def __init__(self, path):
        try:
            with open(path) as file:
                self._parse(file)
        except FileNotFoundError:
            raise SnippetError("File " + path + " not found.")
        except SnippetError:
            raise SnippetError("File not a valid snippet")
        self.path = path


    def _parse(self, file):
        # validate file formatting
        if file.readline() != "---\n":
            raise SnippetError("File not a valid snippet")
        current_line = file.readline()

        # parse frontmatter
        while current_line != "---\n":
            key, value = current_line.split(":", 1)
            self._assign_key_values(key, value.lstrip(" ").rstrip("\n"))
            current_line = file.readline()
        current_line = file.readline()

        # parse description
        while current_line[:3] != "```":
            self.description += current_line
            current_line = file.readline()
        self.description = self.description.lstrip("\n").rstrip("\n")

        # parse actual language of the file (for syntax highlighting)
        self.code_language = current_line.lstrip("```").rstrip("\n")
        current_line = file.readline()

        # parse actual file (the code)
        while current_line != "```\n":
            self.code += current_line
            current_line = file.readline()
        self.code = self.code.rstrip("\n")


    def _assign_key_values(self, key, values):
        if key == "id":
            self.snippet_id = int(values)
        elif key == "tags":
            self.tags = [tag.lstrip(" ").rstrip(" ") for tag in values.split(",")]
        elif key == "title":
            self.title = values.lstrip("\"").rstrip("\"")
        elif key == "lang":
            self.language = values


    def set_id(self, snippet_id):
        with open(self.path, "r+") as file:
            file.readline()
            old_file = file.read()
            file.seek(0, 0)
            file.write("---\nid: " + str(snippet_id) + "\n" + old_file)
        self.snippet_id = snippet_id


    def display(self):
        lexer = get_lexer_by_name(self.code_language, stripall=True)
        formatter = Terminal256Formatter()
        code = highlight(self.code, lexer, formatter)

        print("#" + str(self.snippet_id) + ": \033[1m" + self.title + "\033[0m\n")
        print(self.description + "\n")
        print(code)


    def copy_to_clipboard(self):
        pyperclip.copy(self.code)
        print("Copied snippet #" + str(self.snippet_id) + " to the clipboard.")
