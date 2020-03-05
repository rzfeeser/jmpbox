#!/usr/bin/python3

import requests

gotchar = requests.get("https://www.anapioficeandfire.com/api/characters")
print(gotchar.json())
