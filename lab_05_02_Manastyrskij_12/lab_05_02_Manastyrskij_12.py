x = float(input("Введите положительное число = "))

#def frange(start, stop, step):
#    i = start
#    while i < stop:
#        yield i
#        i += step

#for y in frange(0.0,x,0.001):
#    if y * y > x:
#        break
#print(f"{y:.3f}^2 = {y*y:.3f} > {x:.3f}")

for y in (z / 1000 for z in range(0, int(x) * 1000)):
    if y * y > x:
        break
print(f"{y:.3f}^2 = {y*y:.3f} > {x:.3f}")

# Задано положительное вещественное число. Определить наименьшее 
# положительное число, квадрат которого превосходит данное.
