from itertools import product
from functools import reduce

N = int(input())

a = [3, 5, 17, 257, 65537, 4294967297]

result = -2
for i in range(30):
    for p in product([True, False], repeat=6):
        if reduce(lambda x, y: x * y, (a[i] for i in range(6) if p[i]), 1) * (2 ** i) > N:
            continue
        result += 1
print(result)
