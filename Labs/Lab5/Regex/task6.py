import re

def rep_colon(s):
    return re.sub(r"[ .,]", ":", s)

str = str(input())
new_str = rep_colon(str)
print(new_str)