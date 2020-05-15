N, K = map(int, input().split())

if N % 2 == 0:
    print(min(K + 1, N // 2))
else:
    print(min(K + 1, N))
