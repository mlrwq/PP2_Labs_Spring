import re

def upc_lowc(s):
    pattern = r"A[A-Z][a-z]+"
    if re.search(pattern, s):
        return True
    else:
        return False
    
str = str(input())
print(upc_lowc(str))