N = int(input())
S = input()
a = list(map(int, input().split()))

result = 0
minv = 0
maxv = 0
v = 0
for i in range(N):
    if S[i] == 'R':
        v += a[i]
    elif S[i] == 'B':
        v -= a[i]
    result = max(result, abs(v - minv))
    result = max(result, abs(v - maxv))
    minv = min(minv, v)
    maxv = max(maxv, v)
print(result)
