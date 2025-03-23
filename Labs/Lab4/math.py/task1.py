import math
def degree_to_radian(degree):
    return (degree * math.pi) / 180

Degree = float(input())
radian = round(degree_to_radian(Degree), 6)

print(radian)
