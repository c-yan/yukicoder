N, K = map(int, input().split())

if K == 0 or K > N:
    print(0)
elif K - 1 == N - K:
    print(N - 1)
else:
    print(N - 2)
