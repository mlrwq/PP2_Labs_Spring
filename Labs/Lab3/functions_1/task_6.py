def rev_str(s):
    w = s.split()
    for i in range (len(w)-1, -1, -1):
        print(w[i], end = " ")


my_string = input()
rev_str(my_string)
