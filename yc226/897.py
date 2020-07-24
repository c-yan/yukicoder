Q = int(input())
for _ in range(Q):
    N, K = map(int, input().split())
    if K == 1:
        print(N - 1)
    else:
        N -= 1
        result = 0
        t = K
        while N > 0:
            N -= t
            result += 1
            t *= K
        print(result)
