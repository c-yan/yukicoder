from sys import stdin

readline = stdin.readline
m = 1000000007

N = int(readline())
result = 0
for _ in range(N):
    C, D = map(int, readline().split())
    result += (C + 1) // 2 % m * D % m
    result %= m
print(result)
