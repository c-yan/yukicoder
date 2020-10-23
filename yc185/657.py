from sys import stdin

readline = stdin.readline

T = [0] * (10 ** 6 + 1)
T[4] = 1
for k in range(5, 10 ** 6 + 1):
    T[k] = T[k - 1] + T[k - 2] + T[k - 3] + T[k - 4]
    T[k] %= 17

Q = int(readline())

result = []
for _ in range(Q):
    n = int(readline())
    result.append(T[n])
print(*result, sep='\n')
