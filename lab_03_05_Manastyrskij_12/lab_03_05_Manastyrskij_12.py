x, y = map(float, input("Введите X и Y = ").split())
if ((x >= y ** 2 or x <= -y ** 2) and y >= x ** 2) or ((x >= y ** 2 or x <= -y ** 2) and y <= -x ** 2):
    print(f"Попадание при X = {x}\t Y = {y}")
else:
    print(f"Нет попадания при X = {x}\t Y = {y}")
