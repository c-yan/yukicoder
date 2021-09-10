N, *A = map(int, open(0).read().split())

x = 0
for a in A:
    x |= a

for i in range(x.bit_length() + 1):
    if (x >> i) & 1 == 0:
        print(1 << i)
        break
