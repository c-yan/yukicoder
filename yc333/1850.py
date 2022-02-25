from sys import stdin

readline = stdin.readline

T = int(readline())
for _ in range(T):
    X, Y = map(int, readline().split())
    if Y <= X or X > 4:
        print('Yes')
    else:
        print('No')
