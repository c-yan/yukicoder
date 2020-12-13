A, B = map(int, input().split())

result = 10 ** 12
for a in range(1000):
    for b in range(1000):
        if a + b == 0:
            continue
        x = int((100 * a) / (a + b) + 0.5)
        y = int((100 * b) / (a + b) + 0.5)
        if x == A and y == B:
            result = min(result, a + b)
print(result)
