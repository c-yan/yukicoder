N = int(input())
A = list(map(int, input().split()))

l = A[::2]
r = A[1::2]
for i in range(N - 1):
    l[i + 1] += l[i]
    r[i + 1] += r[i]

result = l[N - 1] - r[N - 1]
result = max(result, r[N - 1] - l[N - 1])
for i in range(1, N):
    t = l[N - 1 - i] + (r[N - 1] - r[N - 1 - i])
    t -= r[N - 1 - i] + (l[N - 1] - l[N - 1 - i])
    result = max(result, t)
print(result)
