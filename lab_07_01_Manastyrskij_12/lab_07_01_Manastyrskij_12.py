from random import randint

x1 = set()
x2 = set()
x3 = set()

x1_n, x2_n, x3_n = map(int, input("Введите мощности множеств X1, X2, X3: ").split())

for i in range(0, x1_n):
    x1.add(randint(0, 1000))

for i in range(0, x2_n):
    x2.add(randint(0, 1000))

for i in range(0, x3_n):
    x3.add(randint(0, 1000))

y = (x1.difference(x2)).union(x2.intersection(x3))
print(f"Множество Х1 = {x1}\nМножество Х2 = {x2}\nМножество Х3 = {x3}\nМножество Y = {y}\nМощность множества Y = {len(y)}")

z = y.copy()

for elem in z:
    flag = False
    for i in range(2, elem):
        if elem % i == 0:
            flag = True
        if flag:
            y.discard(elem)
            break            

print(f"Простые числа в множестве Y = {y}\nМощность множества Y = {len(y)}")
