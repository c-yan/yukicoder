l, r, n = map(int, input().split())

a = [(r + 1) // n] * n
for i in range((r + 1) % n):
    a[i] += 1

b = [l // n] * n
for i in range(l % n):
    b[i] += 1

for i in range(n):
    a[i] -= b[i]

print(*a, sep='\n')
