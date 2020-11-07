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
    if start == 0:
        return bit_sum(bit, stop - 1)
    else:
        return bit_sum(bit, stop - 1) - bit_sum(bit, start - 1)


N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

t = {j: i for i, j in enumerate(sorted(set(a + b)))}
bit = [0] * len(t)

a.sort()
result = 0
for i in range(N):
    bit_add(bit, t[b[i]], 1)
    result += bit_query(bit, 0, t[a[i]])
print(result)
