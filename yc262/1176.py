from math import ceil, log

A = int(input())

result = float('inf')
for i in range(2, 100):
    result = min(result, i * ceil(log(A, i)))
print(result)
