from sys import setrecursionlimit, stdin

readline = stdin.readline
setrecursionlimit(10 ** 6)

N, Q = map(int, readline().split())

links = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, readline().split())
    links[a - 1].append(b - 1)
    links[b - 1].append(a - 1)

visited = [False] * N
subnodes = [0] * N


def f(i):
    visited[i] = True
    result = 1
    for j in links[i]:
        if visited[j]:
            continue
        result += f(j)
    subnodes[i] = result
    return result


f(0)

result = []
t = 0
for _ in range(Q):
    p, x = map(int, readline().split())
    t += subnodes[p - 1] * x
    result.append(t)
print(*result, sep='\n')
