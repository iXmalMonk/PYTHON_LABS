n1 = int(input("Введите целое число = "))
n2 = 0
while n1 > 0:
    n3 = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + n3
print(f"Обратное число = {n2}")

# Дано целое положительное число. Вывести его в обратном порядке 
# следования цифр.
