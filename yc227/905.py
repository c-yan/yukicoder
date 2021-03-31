from sys import setrecursionlimit, stdin
from itertools import accumulate

readline = stdin.readline

N = int(readline())
A = list(map(int, readline().split()))
Q = int(readline())

mi = [0] * N
md = [0] * N
for i in range(N - 1):
    if A[i] <= A[i + 1]:
        mi[i + 1] = 1
    if A[i] >= A[i + 1]:
        md[i + 1] = 1
mi = list(accumulate(mi))
md = list(accumulate(md))

result = []
for _ in range(Q):
    l, r = map(int, readline().split())
    t = ''
    if mi[r] - mi[l] == r - l:
        t += '1'
    else:
        t += '0'
    t += ' '
    if md[r] - md[l] == r - l:
        t += '1'
    else:
        t += '0'
    result.append(t)
print(*result, sep='\n')
