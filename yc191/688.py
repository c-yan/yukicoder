K = int(input())

if K == 0:
    print(1)
    print(0)
    exit()

for N in range(2, 30 + 1):
    for i in range(2, N + 1):
        if 2 ** (N - i) * (i * (i - 1) // 2) != K:
            continue
        print(N)
        print(*([0] * (N - i) + [1] * i))
        exit()
