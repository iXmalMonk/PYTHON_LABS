# Вариант 12
# Манастырский А.С.
# Задача 3.1

x, y, z = map(int, input('Введите (через пробел) 3 числа (x, y, z) = ').split())
print(f"K = {max(max(x, y), min(y, z)) / (max(x, z) ** 2):.3f}")

# k = max(max(x, y), min(y, z)) / (max(x, z) ** 2)