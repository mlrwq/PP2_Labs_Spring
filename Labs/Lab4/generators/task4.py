def squares(a, b):
    for i in range(a, b):
        yield i**2

fr = int(input())
to = int(input())

for i in squares(fr, to):
    print(i)