from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

N, K = map(int, input().split())


@lru_cache(maxsize=None)
def f(n, k):
    if k > K:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        result = f(n // 2, k + 1)
        if result:
            return True
    if n > 3:
        return f(n - 3, k + 1)
    return False


if f(N, 0):
    print('YES')
else:
    print('NO')
