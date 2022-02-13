import math
x = float(input('X = '))
y = float(input('Y = '))
print(f"F = {math.atan((x + 1) ** (1 / 3) + math.cos(math.pi * x) / abs(x ** 2 + y)):.3f}")