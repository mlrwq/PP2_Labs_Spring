n = int(input())
squares = (x**2 for x in range(1, n+1))

for i in squares:
    print(i)