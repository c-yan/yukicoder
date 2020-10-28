N = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

m = float('inf')
for i in range(N):
    m = min(m, X[i] + Y[i])

result = []
result.append(m)
result.append(0)
for i in range(N):
    result.append(min(X[i], m))
result.append(m)
print(*result, sep='\n')
