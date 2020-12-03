def enumerate_primes(n):
    if n < 2:
        return []
    sieve = list(range(n + 1))
    result = [2]
    for i in range(4, n + 1, 2):
        sieve[i] = 2
    m = int(n ** 0.5)
    if m % 2 == 0:
        m -= 1
    for i in range(3, m + 1, 2):
        if sieve[i] != i:
            continue
        result.append(i)
        for j in range(i * i, n + 1, i * 2):
            if sieve[j] == j:
                sieve[j] = i
    for i in range(m + 2, n + 1, 2):
        if sieve[i] == i:
            result.append(i)
    return result


N = int(input())

if N == 1:
    print(0)
    exit()
elif N == 2:
    print(1)
    exit()

result = 1
ps = enumerate_primes(N)
ops = set(ps[1:])
for r in ps[1:]:
    if r * r - 2 > N:
        break
    if r * r - 2 in ops:
        result += 2
print(result)
