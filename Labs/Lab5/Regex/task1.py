import re

def more_bs(s):
    pattern = r"^ab*$"
    if re.search(pattern, s):
        return True
    else: 
        return False

str = str(input())
print(more_bs(str))