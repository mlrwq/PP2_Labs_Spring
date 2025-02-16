def rev_generator(n):
    for i in range (n, -1, -1):
        yield i

num = int(input())

for i in rev_generator(num):
    print(i)