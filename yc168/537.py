N = int(input())

t = set()
for i in range(1, int(N ** 0.5) + 1):
    if N % i != 0:
        continue
    t.add('%d%d' % (N // i, i))
    t.add('%d%d' % (i, N // i))
print(len(t))
