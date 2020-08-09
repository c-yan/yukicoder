A, B, C, D = map(int, input().split())

if D >= 10:
    print('Impossible')
    exit()

print('Possible')

result = 0
m = 1
c = 0
while B != 0:
    t = min(100 - c, B)
    B -= t
    result += 50 * t * m
    c += t
    if c == 100:
        c = 0
        m *= 2

while A != 0:
    t = min(100 - c, A)
    A -= t
    result += 100 * t * m
    c += t
    if c == 100:
        c = 0
        m *= 2

print(result)
