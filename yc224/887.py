n0 = int(input())

n = n0
nmax = n0
i = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    i += 1
    nmax = max(nmax, n)
print(i)
print(nmax)
