import re

def ins_spaces(s):
    words = re.findall(r"[A-Z][a-z]*", s)
    res = ""

    for i in words:
        res += i + " "
    
    return res.strip()

str = str(input())
print(ins_spaces(str))