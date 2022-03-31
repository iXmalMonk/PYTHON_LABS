from math import exp
from math import sqrt

print("_________________________________\n")

for x in (z / 10 for z in range(-9,19)):
    if abs(exp(1) + 2 * x * x * x + 5 * x) > 1.5:
        print(f"| X = {x:>4} | Y = {sqrt(x * x * x + 2.5 * x + exp(2)):.3f} |  > 1.5 |")
    elif abs(exp(1) + 2 * x * x * x + 5 * x) <= 1.5:
        print(f"| X = {x:>4} | Y = {1 / (1 - x * x * x - 2.5 * x) + sqrt(exp(1)):.3f} | <= 1.5 |")

print("_________________________________\n")

print("x * x * x + 2.5 * x + exp(2)  > 1.5 | sqrt(x * x * x + 2.5 * x + exp(2))\n")
print("x * x * x + 2.5 * x + exp(2) <= 1.5 | 1 / (1 - x * x * x - 2.5 * x) + sqrt(exp(1))\n")