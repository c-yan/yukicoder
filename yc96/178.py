N = int(input())

t = [None] * N
for i in range(N):
    a, b = map(int, input().split())
    t[i] = a + 4 * b

r = t[0] % 2
if any(x % 2 != r for x in t[1:]):
    print(-1)
    exit()

m = max(t)
print(sum((m - x) // 2 for x in t))
