from math import *
def is_prime(n):
    if n < 2:
        return False
    for i in range (2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False  
   
    return True

class List():
    def __init__(self, list):
        self.list = list

    def filter(self):
        print(list(filter(lambda n : is_prime(n), self.list)))

my_list = []
a = int(input())

for i in range (a):
    x = int(input())
    my_list.append(x)

my_list = List(my_list)
my_list.filter()
