from itertools import accumulate

N = int(input())
S = input()
a = list(map(int, input().split()))

for i in range(N):
    if S[i] == 'R':
        continue
    a[i] = -a[i]

result = 0
minv = 0
maxv = 0
for v in list(accumulate(a)):
    result = max(result, abs(v - minv))
    result = max(result, abs(v - maxv))
    minv = min(minv, v)
    maxv = max(maxv, v)
print(result)
