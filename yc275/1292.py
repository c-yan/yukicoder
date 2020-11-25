S = input()

x, y = 0, 0
t = {(0, 0)}

s0 = [(-1, 0), (0, -1), (1, 0), (-1, 0), (0, 1), (1, 0)]
s1 = [(-1, 0), (0, 1), (1, 0), (-1, 0), (0, -1), (1, 0)]

for ch in S:
    if ch == 'a':
        if y % 2 == 0:
            dx, dy = s0[x % 6]
        else:
            dx, dy = s1[x % 6]
    elif ch == 'b':
        if y % 2 == 0:
            dx, dy = s0[(x + 4) % 6]
        else:
            dx, dy = s1[(x + 4) % 6]
    elif ch == 'c':
        if y % 2 == 0:
            dx, dy = s0[(x + 2) % 6]
        else:
            dx, dy = s1[(x + 2) % 6]
    x += dx
    y += dy
    t.add((x, y))
print(len(t))
