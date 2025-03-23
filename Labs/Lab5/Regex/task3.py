import re

def lowc_und(s):
    pattern = r"[a-z]+_[a-z]+"
    if re.search(pattern, s):
        return True
    else:
        return False
    
str = str(input())
print(lowc_und(str))