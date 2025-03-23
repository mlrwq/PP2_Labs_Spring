from time import *
from math import *

number = int(input())
miliseconds = int(input())

sleep(miliseconds/1000)
sqrt_num = sqrt(number)

print(f"Square root of {number} after {miliseconds} miliseconds is {sqrt_num}")
