x = int(input('Введите X [-6;7] = '))
if -6 <= x < -4:
    print(f"Y = {0.5 * x + 3:.3f}")
elif -4 <= x < 0:
    print(f"Y = {-(-x ** 2 - 4 * x) ** 0.5 + 1:.3f}")
elif 0 <= x < 2:
    print(f"Y = {(-x ** 2 + 2 * x) ** 0.5 + 1:.3f}")
elif 2 <= x < 3:
    print(f"Y = {x - 1:.3f}")
elif 3 <= x < 7:
    print("Y = 2")
else:
    print("Введен неверный интервал!")


# y = kx + b
# 0 = k * -6 + b    b = 3
# 1 = k * -4 + b    k = 0.5
# y = 0.5 * x + 3
# ==========
# (x - a) ** 2 + (y - b) ** 2 = R ** 2
#
# (x + 2) ** 2 + (y - 1) ** 2 = 2 ** 2
# y = -(x ** 2 - 4 * x) ** 0.5 + 1
# ----------
# (x - 1) ** 2 + (y - 1) ** 2 = 1 ** 2
# y = (-x ** 2 + 2 * x) ** 0.5 + 1
# ==========
# 1 = k * 2 + b     b = -1
# 2 = k * 3 + b     k = 1
# y = 1 * x - 1