import json

from initializr import Initializr

with open('input.json', 'r') as f:
    inp = json.load(f)

# todo: validate input

init = Initializr(inp)
init.make_curl()
init.unzip()