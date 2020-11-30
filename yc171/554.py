n = int(input())

m = 1000000007

b = 1
c = 0

for i in range(2, n):
    if i % 2 == 0:
        t = i * b
        c += t
        c %= m
    else:
        t = i * c
        b += t
        c %= m

if n == 1:
    print(1)
elif n % 2 == 0:
    print(n * b % m)
else:
    print(n * c % m)
