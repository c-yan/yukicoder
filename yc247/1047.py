A, B = map(int, input().split())

N = 0
for i in range(1, 10000):
    N = A * N + B
    if N == 0:
        print(i)
        exit()
print(-1)
