def solve(numheads, numlegs):
    for chickens in range (numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            print (chickens, rabbits)


Numheads = int(input())
Numlegs = int(input())
solve(Numheads, Numlegs)