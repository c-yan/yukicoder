m, *A = map(int, open(0).read().split())


def f(a):
    return bin(a + 1)[3:].replace('0', 'L').replace('1', 'R')


for a in A:
    print(f(a))
