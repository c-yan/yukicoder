V, D = map(int, input().split())

t = [[0] * V for _ in range(V)]
if D == 1:
    t = [[1] * V for _ in range(V)]
else:
    for i in range(V):
        t[0][i] = 1
        t[i][0] = 1
for i in range(V):
    print(*t[i], sep='')
