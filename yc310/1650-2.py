N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []
for i in range(N):
    if A[i] <= B[i]:
        continue
    for _ in range(A[i] - B[i]):
        result.append('%d L' % (i + 1))
for i in range(N - 1, -1, -1):
    if A[i] >= B[i]:
        continue
    for _ in range(B[i] - A[i]):
        result.append('%d R' % (i + 1))
print(len(result))
print(*result, sep='\n')
