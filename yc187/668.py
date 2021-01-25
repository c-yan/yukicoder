N = input()

a = int(N[0])
b = int(N[1])
c = len(N) - 1

if int(N[2]) >= 5:
    b += 1
if b == 10:
    b = 0
    a += 1
if a == 10:
    a = 1
    c += 1

print('%d.%d*10^%d' % (a, b, c))
