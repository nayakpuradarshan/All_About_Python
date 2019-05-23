import re
import pprint
import xlsxwriter


p = re.compile("^(((2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9]))$")

f = open("list_ip_add")

D = {}

for ip in f:
    ip = ip.strip()
    r = p.search(ip)
    if r:
        D[ip] = "Pass"
    else:
        D[ip] = "Fail"

pprint.pprint(D, indent=4)


workbook = xlsxwriter.Workbook('ipvalidation.xlsx') 

wsheet = workbook.add_worksheet("ip")

wsheet.write(0, 0, "IP Address")
wsheet.write(0, 1, "Valid")

row=1
col=0


for k in D:
    wsheet.write(row, col, k)
    wsheet.write(row, col + 1, D[k])
    row=row+1
    col=0


workbook.close()
