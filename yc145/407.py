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


N, L = map(int, input().split())

t = L // (N - 1)
result = 0
for d in enumerate_primes(t):
    result += L - d * (N - 1) + 1
print(result)
