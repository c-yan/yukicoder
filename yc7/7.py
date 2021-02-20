from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(10 ** 6)


def make_prime_table(n):
    sieve = list(range(n + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(4, n + 1, 2):
        sieve[i] = 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i] != i:
            continue
        for j in range(i * i, n + 1, i * 2):
            if sieve[j] == j:
                sieve[j] = i
    return sieve


N = int(input())

prime_table = make_prime_table(N)
prime_numbers = []
for i in range(N + 1):
    if prime_table[i] == i:
        prime_numbers.append(i)


@lru_cache(maxsize=None)
def f(n):
    for p in prime_numbers:
        if n - p <= 1:
            return False
        t = f(n - p)
        if not t:
            return True


if f(N):
    print('Win')
else:
    print('Lose')
