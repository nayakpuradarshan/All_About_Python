import requests
import re
import time
import os



page = requests.get("https://en.wikipedia.org/wiki/List_of_Indian_film_actresses")


f = open("list_of_actresses.html", "wb")
f.write(page.text.encode())
f.close()



f = open("list_of_actresses.html", "rb")
model_name = open("list_of_models", "w")

for line in f:
	m = re.search(b'<li><a href="/wiki/\w+" title=".+">(\w+ *\w*)</a>', line)
	if m:
		model_name.write(m.groups()[0].decode() + "\n")
model_name.close()


os.mkdir("model")
f = open("list_of_actresses.html", "rb")

for line in f:
	m = re.search(b'<li><a .*href="(/wiki/\w+)" title=".+">(\w+ *\w*)</a>', line)
	if m:
		if m.groups()[1].startswith(b"I"):
			url = b"https://en.wikipedia.org/" + m.groups()[0]
			page = requests.get(url.decode())
			
			f = open(br"model\\" + m.groups()[1], "wb")
			f.write(page.text.encode())
			f.close()
			time.sleep(5)
f.close()
