from decimal import Decimal

a, b, S = input().split()

a = int(a)
b = int(b)
S = Decimal(S[3:])

a -= 9

S *= 60
a += S // 60
b += S % 60

if b >= 60:
    a += 1
    b -= 60
elif b < 0:
    a -= 1
    b += 60
if a < 0:
    a += 24
a %= 24

print('%02d:%02d' % (a, b))
