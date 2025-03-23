import re

def a_anyt_b(s):
    pattern = r"a.*b"
    if re.search(pattern, s):
        return True
    else:
        return False
    
str = str(input())
print(a_anyt_b(str))