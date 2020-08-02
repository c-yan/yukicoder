def make_prime_table(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not sieve[i]:
            continue
        for j in range(i * i, n + 1, i):
            sieve[j] = False
    return sieve


def main():
    readline = open(0).readline

    prime_table = make_prime_table(5 * 10 ** 6)

    T = int(readline())
    result = []
    for _ in range(T):
        A, P = map(int, readline().split())
        if not prime_table[P]:
            result.append(-1)
        else:
            if A % P == 0:
                result.append(0)
            else:
                result.append(1)
    print(*result, sep='\n')


main()
