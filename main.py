import json

from entitycreator import create_entities
from initializr import initialize_project
from javaconverterstyler import JavaConverterStyler


def get_input():
    with open('input.json', 'r') as f:
        return json.load(f)


def get_coder():
    return JavaConverterStyler(inp.get("indentation_space_count"),
                               inp.get("open_curly_brackets_same_line"),
                               inp.get("beautify_with_spaces"),
                               inp.get("beautify_with_blank_lines"))


inp = get_input()
# todo: validate input
initialize_project(inp)
java_coder = get_coder()
create_entities(java_coder, inp.get("entities"), inp.get("app_name"))
