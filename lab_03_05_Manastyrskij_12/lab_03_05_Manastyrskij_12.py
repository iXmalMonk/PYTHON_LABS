x, y = map(float, input("Введите X и Y = ").split())
if x * y <= 1 and x > y ** 2 and y > x ** 2:
    print(f"Попадание при X = {x}\t Y = {x}")
elif x * y <= 1 and x < -y ** 2 and y > x ** 2:
    print(f"Попадание при X = {x}\t Y = {x}")
elif x * y <= 1 and x > y ** 2 and y < -x ** 2:
    print(f"Попадание при X = {x}\t Y = {x}")
elif x * y <= 1 and x < -y ** 2 and y < -x ** 2:
    print(f"Попадание при X = {x}\t Y = {x}")
else:
    print(f"Нет попадания при X = {x}\t Y = {x}")
