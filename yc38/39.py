N = input()

result = int(N)
for i in range(len(N) - 1):
    for j in range(i + 1, len(N)):
        t = list(N)
        a, b = t[i], t[j]
        t[i], t[j] = b, a
        result = max(result, int(''.join(t)))
print(result)
