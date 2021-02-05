def tokenize(s):
    t = ''
    for c in s:
        if c not in '+*':
            t += c
        else:
            yield int(t)
            t = ''
            yield c
    yield int(t)


S = input()
s = []
for t in tokenize(S):
    s.append(t)
    if len(s) != 3:
        continue
    b = s.pop()
    op = s.pop()
    a = s.pop()
    if op == '+':
        s.append(a * b)
    elif op == '*':
        s.append(a + b)
print(s.pop())
