import re
import xlsxwriter


"""
import requests


r = requests.get("https://en.wikipedia.org/wiki/List_of_American_film_actresses")

f = open("list_of_actresses", "w")
f.write(r.text)
f.close()
"""

f = open("list_of_actresses")

p = re.compile('^<li><a href="/wiki/.*" title=".*">(.*)</a> born .*> \(age&#160;([0-9]+)\)</span></li>$')

workbook = xlsxwriter.Workbook('actress.xlsx') 
wsheet = workbook.add_worksheet("Hollywood")
wsheet.write(0, 0, "Actress")
wsheet.write(0, 1, "Age")
row=1
col=0

for line in f:
    r = p.search(line)
    if r:
        name = r.groups()[0]
        age  = int(r.groups()[1])
        if 30 <= age <= 40:
            wsheet.write(row, col, name)
            wsheet.write(row, col+1, age)
            row=row+1
            col=0

workbook.close()
