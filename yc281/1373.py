N = int(input())

i = 0
while N != 0:
    N >>= 1
    i += 1
print(1 << (i - 1))
