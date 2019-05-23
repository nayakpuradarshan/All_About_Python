import requests
import re
import time
import os

page = requests.get("https://en.wikipedia.org/wiki/List_of_Indian_film_actors")

f = open("list_of_actresses.html", "wb")
f.write(page.text.encode())
f.close()