N = int(input())
A = [input().split() for _ in range(N)]

t = [True] * N
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if A[i][j] != 'nyanpass':
            t[j] = False

if t.count(True) != 1:
    print(-1)
else:
    print(t.index(True) + 1)
