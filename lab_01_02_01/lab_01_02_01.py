p = float(input('P = '))
k = float(input('K = '))
t = float(input('T = '))
print(f"H = {(p + k) ** 2 / p * k ** 0.5 / (k - p) / t ** 2:.3f}")