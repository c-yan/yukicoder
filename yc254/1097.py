from sys import stdin
readline = stdin.readline

N = int(readline())
A = list(map(int, readline().split()))

X = 0
b = [-1]
c = [X]
used = set()
while True:
    r = X % N
    X += A[r]
    if r in used:
        break
    used.add(r)
    b.append(r)
    c.append(X)
b.append(r)
c.append(X)
loop_start = b.index(b[-1])
loop_len = len(b) - loop_start

Q = int(readline())
for _ in range(Q):
    K = int(readline())
    if K < len(b):
        print(c[K])
    else:
        K -= loop_start
        a = K // loop_len
        K %= loop_len
        K += loop_start
        print(b[K] + K * (c[-1] - c[loop_start]))
