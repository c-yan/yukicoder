from sys import stdin

readline = stdin.readline

N = int(readline())
S = list(readline()[:-1])
T = list(readline()[:-1])
Q = int(readline())

p = 0
while p < N and S[p] == T[p]:
    p += 1

result = []
for _ in range(Q):
    c, x, y = readline().split()
    x = int(x) - 1
    if  c == 'S':
        S[x] = y
    elif c == 'T':
        T[x] = y
    if x < p and S[x] != T[x]:
        p = x
    elif x == p and S[x] == T[x]:
        while p < N and S[p] == T[p]:
            p += 1

    if p == N:
        result.append('=')
    elif S[p] > T[p]:
        result.append('>')
    elif S[p] < T[p]:
        result.append('<')
print(*result, sep='\n')
