from heapq import heapify, heappop, heappush

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))

numbers = [Z, Y, X]
bills = [10000, 5000, 1000]

A = [-n for n in A]
heapify(A)

for i in range(3):
    n = numbers[i]
    b = bills[i]

    while A:
        if n == 0:
            break
        x = -heappop(A)
        if x >= b:
            t = min(x // b, n)
            n -= t
            x -= b * t
            heappush(A, -x)
        else:
            n -= 1

if len(A) == 0:
    print('Yes')
else:
    print('No')
