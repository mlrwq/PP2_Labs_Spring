import math
def Reg_Polygon_Area(n, a):
    return (n * a**2) / (4 * math.tan(math.pi / n))

num_sides = int(input())
length = int(input())

print(round(Reg_Polygon_Area(num_sides, length), 1))