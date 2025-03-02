str = str(input())

up_count = sum(1 for i in str if i.isupper())
low_count = sum(1 for i in str if i.islower())

print(up_count, low_count)