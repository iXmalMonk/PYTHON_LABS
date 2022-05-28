from math import sqrt

while True:
    str = input('Введите положительное число (минимум 10 знаков)\nN: ')
    if str.isdigit() and len(str) >= 10 and int(str) > 0:
        break

list = [int(number) for number in str]
list = [number * number for number in list]
print(f"{sqrt(sum(list)/len(str)):.3f}")

# 12. Дано целое положительное число. Определить среднее квадратическое
# его цифр.

