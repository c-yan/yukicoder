m = 1000000007


def make_factorial_table(n):
    result = [0] * (n + 1)
    result[0] = 1
    for i in range(1, n + 1):
        result[i] = result[i - 1] * i % m
    return result


N, *A = map(int, open(0).read().split())

A.sort()

if A[0] == 0:
    print(-1)
    exit()

if A[-1] >= 4:
    print(m)
    exit()

fac = make_factorial_table(3)

t = 1
for a in A:
    t *= pow(a, fac[a])
    if t > m:
        break
print(m % t)
