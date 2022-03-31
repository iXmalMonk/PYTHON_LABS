from math import sin

y = int(input("Введите [Y] = "))
p = 1.0

for x in range(5, 12):
    p *= (x*x*x + sin(x))

print(f"F = {p * (y-1):.3f}")

#           11
# (y - 1) * P (x*x*x + sin(x))
#           x = 5