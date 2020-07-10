N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

t = [0] * 101
for i in range(N):
    t[b[i]] += a[i]

if t[0] == max(t):
    print('YES')
else:
    print('NO')
