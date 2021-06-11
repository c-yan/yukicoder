N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N * M):
    if A[i % N] != B[i % M]:
        continue
    print(i + 1)
    break
else:
    print(-1)
