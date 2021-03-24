from itertools import product

N = int(input())
s = [input() for _ in range(N)]


def f(p):
    t = 0
    wins = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            if s[i][j] != p[t] and s[i][j] != '-':
                return 10 ** 18
            if p[t] == 'o':
                wins[i] += 1
            elif p[t] == 'x':
                wins[j] += 1
            t += 1
    a = wins[0]
    wins = sorted(set(wins), reverse=True)
    for i in range(N):
        if wins[i] != a:
            continue
        return i + 1


result = 10 ** 18
for p in product('ox', repeat=N * (N - 1) // 2):
    result = min(result, f(p))
print(result)
