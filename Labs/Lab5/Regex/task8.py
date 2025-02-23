import re

def spl_upc(s):
    res = re.findall(r"[A-Z][a-z]*", s)
    return res

str = str(input())
print(spl_upc(str))