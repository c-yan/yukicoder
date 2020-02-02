s = input()

t = []
for c in s:
    if c != c.lower():
        t.append(c.lower())
    elif c != c.upper():
        t.append(c.upper())
    else:
        t.append(c)
print(''.join(t))
