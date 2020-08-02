# PyPy でのみ AC
def make_prime_table(n):
    sieve = list(range(n + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] != i:
            continue
        for j in range(i * i, n + 1, i):
            if sieve[j] == j:
                sieve[j] = i
    return sieve


readline = open(0).readline

prime_table = make_prime_table(5 * 10 ** 6)

T = int(readline())
result = []
for _ in range(T):
    A, P = map(int, readline().split())
    if prime_table[P] != P:
        result.append(-1)
    else:
        if A % P == 0:
            result.append(0)
        else:
            result.append(1)
print(*result, sep='\n')
