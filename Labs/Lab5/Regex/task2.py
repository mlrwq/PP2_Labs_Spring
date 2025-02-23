import re

def two_three_bs(s):
    pattern = r"^ab{2,3}"
    if re.search(pattern, s):
        return True
    else:
        return False
    
str = str(input())
print(two_three_bs(str))