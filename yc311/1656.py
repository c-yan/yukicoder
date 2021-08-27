from sys import stdin

readline = stdin.readline

T = int(readline())

result = []
for _ in range(T):
    A, B = map(int, readline().split())
    result.append((A + 1) * B)
print(*result, sep='\n')
