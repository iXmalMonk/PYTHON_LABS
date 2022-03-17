x = int(input("Введите [X] = "))
e = float(input("Введите точность [E] = "))

minus = -1
x_5 = (5 * x) ** 3 # (5 * x) * (5 * x) * (5 * x)
fact = 2
fact_i = 3
amount = 0
s = minus * x_5 / fact

#n = 2

while abs(s) > e:
    amount += s
    minus *= -1
    x_5 *= 5 * x
    fact *= fact_i
    fact_i += 1
    
    #n += 1
    
    s = minus * x_5 / fact

print(f"Сумма = {amount:.5f}")

#print(n)

# inf
# E     (-1)^n * (5*x)^n / (n-1)!
# n = 3