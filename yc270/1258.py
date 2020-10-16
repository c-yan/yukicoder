from sys import stdin

readline = stdin.readline
m = 1000000007

S = int(readline())
div2 = pow(2, m - 2, m)
for _ in range(S):
    N, M, X = map(int, readline().split())
    a = pow(M + 1, N, m)
    b = pow(M - 1, N, m)
    if (N + X) % 2 == 0:
        print((a + b) * div2 % m)
    else:
        print((a - b) * div2 % m)
