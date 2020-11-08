N = int(input())
K = int(input())


def f(x):
    if x > 2 * N:
        return 0
    if x - 1 < N:
        return x - 1
    return (x - 1) - ((x - 1) - N) * 2


result = 0
for i in range(2, int(K ** 0.5) + 1):
    if K % i != 0:
        continue
    if i == K // i:
        result += f(i) * f(K // i)
    else:
        result += f(i) * f(K // i) * 2
print(result)
