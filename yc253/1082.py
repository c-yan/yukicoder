N = int(input())
A = list(map(int, input().split()))

result = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        result = max(result, A[i] ^ A[j])
print(result)
