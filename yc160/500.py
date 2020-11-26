from functools import reduce

N = int(input())

if N >= 50:
    print('0' * 12)
else:
    print(str(reduce(lambda x, y: x * y, range(1, N + 1)))[-12:])
