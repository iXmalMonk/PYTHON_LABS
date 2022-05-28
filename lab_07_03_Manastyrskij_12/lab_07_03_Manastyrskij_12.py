from random import uniform

while(True):
    n = int(input("Введите размер массива [3;20]: "))
    if n > 2 and n < 21:
        break

arr = []

for i in range(0, n):
    arr.append(uniform(1, n))

print(f"Array = {arr}")

prod = 1

for i in range(0, n):
    prod *= arr[i]

print(f"Произведение = {prod:.3f}")