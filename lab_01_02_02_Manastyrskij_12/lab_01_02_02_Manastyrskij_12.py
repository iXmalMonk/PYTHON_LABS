# Вариант 12
# Манастырский А.С.
# Задача 1.2.2

import math
a, b = map(float,input('Введите(через пробел) 2 числа (a, b) = ').split())
print(f"y = {((18 + a) * math.log(2*b))**(1/7) + math.e ** (9/12/a):.3f}")

# y = ((18 + a) * math.log(2*b))**(1/7) + math.e ** (9/12/a)