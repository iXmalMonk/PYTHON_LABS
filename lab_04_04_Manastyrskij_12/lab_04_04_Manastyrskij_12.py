while(True):
    num = input("Введите натуральное число = ")
    if 0 < int(num) < 1000000000 and num.isdigit():
        num = int(num)
        break
num_max = 0
while num > 0:
    dig = num % 10
    num = num // 10
    if dig % 3 == 0 and dig > num_max:
        num_max = dig
    if num_max != 0 and num == 0 or num_max == 9:
        print(f"Максимальная цифра кратная '3' = {num_max}")
        break
else:
    print("Нет цифр кратных '3'")

# На обработку поступает натуральное число, не превышающее 10^9. 
# Нужно написать программу, которая выводит на экран максимальную цифру 
# числа, кратную 3. Если в числе нет цифр, кратных 3, требуется на экран вывести 
# сообщение об этом.