def bit_add(bit, i, x):
    i += 1
    n = len(bit)
    while i <= n:
        bit[i - 1] += x
        i += i & -i


def bit_sum(bit, i):
    result = 0
    i += 1
    while i > 0:
        result += bit[i - 1]
        i -= i & -i
    return result


def bit_query(bit, start, stop):
    return bit_sum(bit, stop - 1) - bit_sum(bit, start - 1)


def bit_add_m(bit, i, x):
    i += 1
    n = len(bit)
    while i <= n:
        bit[i - 1] += x
        bit[i - 1] %= m
        i += i & -i


def bit_sum_m(bit, i):
    result = 0
    i += 1
    while i > 0:
        result += bit[i - 1]
        result %= m
        i -= i & -i
    return result


def bit_query_m(bit, start, stop):
    return (bit_sum(bit, stop - 1) - bit_sum(bit, start - 1)) % m


N, *A = map(int, open(0).read().split())

m = 998244353

to = {x: i for i, x in enumerate(sorted(set(x for x in A)))}

n = len(to.keys())
lbitc = [0] * n
rbitc = [0] * n
lbits = [0] * n
rbits = [0] * n
for x in A[2:]:
    i = to[x]
    bit_add(rbitc, i, 1)
    bit_add_m(rbits, i, x)
bit_add(lbitc, to[A[0]], 1)
bit_add_m(lbits, to[A[0]], A[0])

result = 0
for i in range(1, N - 1):
    x = to[A[i]]
    y = bit_query(lbitc, x + 1, n)
    z = bit_query(rbitc, 0, x)
    result += bit_query_m(lbits, x + 1, n) * z
    result += A[i] * (y * z)
    result += bit_query_m(rbits, 0, x) * y
    result %= m
    bit_add(lbitc, x, 1)
    bit_add_m(lbits, x, A[i])
    x = to[A[i + 1]]
    bit_add(rbitc, x, -1)
    bit_add_m(rbits, x, -A[i + 1])
print(result)
