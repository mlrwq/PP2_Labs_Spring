def str_permutation(s, ans = ""):
    if s == "":
        print(ans)
        return
    
    for i in range(len(s)):
        c = s[i]
        r = s[:i] + s[i+1:]
        str_permutation(r, ans + c)

my_string = input()
str_permutation(my_string)