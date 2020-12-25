from functools import lru_cache

K = int(input())


@lru_cache(maxsize=None)
def E(x):
    if x >= K:
        return 0
    return (E(x + 1) + E(x + 2) + E(x + 3) + E(x + 4) + E(x + 5) + E(x + 6)) / 6 + 1


print(E(0))
