import json

from initializr import initialize_project


def get_input():
    with open('input.json', 'r') as f:
        return json.load(f)


inp = get_input()
# todo: validate input
initialize_project(inp)
