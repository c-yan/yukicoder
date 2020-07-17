N, *X = map(int, open(0).read().split())

X = sorted(set(X))

if len(X) == 1:
    print(0)
    exit()

result = float('inf')
for i in range(len(X) - 1):
    result = min(result, X[i + 1] - X[i])
print(result)
