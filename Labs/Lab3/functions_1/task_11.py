def is_polindrome(s):
    c = ""
    for i in s:
        if (i.isdigit() or i.isalpha()):
            c += i.lower()

    if (c == c[::-1]):
        print(True)
    else: print(False)

my_string = input()
is_polindrome(my_string)
