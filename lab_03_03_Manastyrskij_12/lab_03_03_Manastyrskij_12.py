# Вариант 12
# Манастырский А.С.
# Задача 3.3

import math
x = float(input('Введите X = '))
if x <= -2.2:
    print(f"Y = {3 * x * x * x + 2 * x:.3f}")
elif -2.2 <= x <= 3:
    print(f"Y = {math.exp(-2 * x):.3f}")
else:
    print(f"Y = {math.sin(x) ** 2 + x:.3f}")

# task