T = int(input())

t = {}
for i in range(10):
    for j in range(10):
        k = i + j
        if k >= 10:
            k = k // 10 + k % 10
        t['%d%d' % (i, j)] = str(k)

for _ in range(T):
    S = input()
    while len(S) != 1:
        S = ''.join(t[S[i:i+2]] for i in range(len(S) - 1))
    print(S)
