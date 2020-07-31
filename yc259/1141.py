H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())

m = 1000000007

total = 1
rows = [1] * H
cols = [1] * W
totalm = 0
rowsm = [0] * H
colsm = [0] * W
for i in range(H):
    for j in range(W):
        x = A[i][j]
        if x == 0:
            totalm += 1
            rowsm[i] += 1
            colsm[j] += 1
        else:
            total *= x
            total %= m
            rows[i] *= x
            rows[i] %= m
            cols[j] *= x
            cols[j] %= m

result = []
for _ in range(Q):
    r, c = map(lambda x: int(x) - 1, input().split())
    x = A[r][c]
    t = 0
    if x == 0:
        t = 1
    if totalm - rowsm[r] - colsm[c] + t > 0:
        result.append(0)
    else:
        if x == 0:
            result.append(total * pow(rows[r], -1, m) % m * pow(cols[c], -1, m) % m)
        else:
            result.append(total * pow(rows[r], -1, m) % m * pow(cols[c], -1, m) % m * A[r][c] % m)
print(*result, sep='\n')
