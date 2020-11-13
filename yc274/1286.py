D = int(input())


def f(x):
    result = 0
    while x != 0:
        result += x
        x //= 2
        if result >= D:
            break
    return result


for i in range(60, 0, -1):
    t = D * (2 ** (i - 1)) // (2 ** i - 1)
    for j in range(-100, 100):
        if t + j < 0:
            continue
        if f(t + j) == D:
            print(t + j)
            exit()
