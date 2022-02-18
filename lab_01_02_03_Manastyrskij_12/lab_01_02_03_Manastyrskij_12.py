# Вариант 12
# Манастырский А.С.
# Задача 1.2.3

import math
x, y = map(float,input('Введите(через пробел) 2 числа (x, y) = ').split())
print(f"F = {math.atan((x + 1) ** (1 / 3) + math.cos(math.pi * x) / abs(x ** 2 + y)):.3f}")

# F = math.atan((x + 1) ** (1 / 3) + math.cos(math.pi * x) / abs(x ** 2 + y))