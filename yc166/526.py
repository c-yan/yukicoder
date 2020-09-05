N, M = map(int, input().split())

a = 0
b = 1
for i in range(N - 2):
    t = a + b
    a = b
    b = t
    b %= M
print(b)
