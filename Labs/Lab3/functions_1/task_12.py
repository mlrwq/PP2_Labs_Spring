def histogram(list):
    for i in list:
        print("*" * i)

my_list = []
n = int(input())

for i in range (n):
    x = int(input())
    my_list.append(x)

histogram(my_list)