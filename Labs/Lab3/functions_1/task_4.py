from math import sqrt

def is_prime(n):
    if n<2: 
        return False
    for i in range (2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(list):
    new_list = [numb for numb in my_list if is_prime(numb)]
    print (new_list)

    

num = int(input())
my_list = []

for i in range (num):
    numbers = int(input())
    my_list.append(numbers)

filter_prime(my_list)

