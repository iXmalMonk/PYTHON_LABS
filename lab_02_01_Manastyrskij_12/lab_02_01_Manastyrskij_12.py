# Вариант 12
# Манастырский А.С.
# Задача 2.1

a = int(input('Введите сторону квадрата (см) = '))
b, c = map(int,input('Введите(через пробел) 2 стороны прямоугольника (см) = ').split())
print(f"Поместиться прямоугольников в квадрат = {(a * a) // (b * c)}")
print(f"Незанятая площадь (см^2) = {(a * a) % (b * c)}")

# Пусть дан квадрат со стороной а и прямоугольник со сторонами b и с. 
# Сколько таких прямоугольников поместится в квадрат, и какая площадь 
# останется незанятой?