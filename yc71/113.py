from math import sqrt

S = input()

y = 0
x = 0

for s in S:
    if s == 'N':
        y += 1
    elif s == 'E':
        x += 1
    elif s == 'W':
        x -= 1
    elif s == 'S':
        y -= 1

print(sqrt(abs(y) ** 2 + abs(x) ** 2))
