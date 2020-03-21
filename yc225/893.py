N = int(input())

P = [None] * N
m = 0
for i in range(N):
    P[i] = list(map(int, input().split()))
    m = max(m, P[i][0])

result = []
for i in range(1, m + 1):
    for Pi in P:
        if Pi[0] >= i:
            result.append(Pi[i])
print(*result)
