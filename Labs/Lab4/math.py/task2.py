def Trapezoid_Area(a, b, h):
    return ((a+b)*h)/2

base_1 = float(input())
base_2 = float(input())
height = float(input())

print(Trapezoid_Area(base_1, base_2, height))