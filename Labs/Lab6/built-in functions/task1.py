from math import *

n = int(input())
my_list = []

for i in range (n):
    x = int(input())
    my_list.append(x)

print(prod(my_list))