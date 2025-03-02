def isPolindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

str = str(input())

if isPolindrome(str):
    print("Yes")
else:
    print("No")


#the second way

str = str(input())
rev_str = ''.join(reversed(str))

if(rev_str.lower() == str.lower()):
    print("Yes")
else:
    print("No")
