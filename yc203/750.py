N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

for A, B in sorted(AB, key = lambda p: p[0] / p[1], reverse=True):
    print(A, B)
