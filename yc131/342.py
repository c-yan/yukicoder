S = input()

d = {}
c = 0
t = ''
for i in range(len(S)):
    if S[i] != 'ｗ':
        if c > 0:
            if t != '':
                d.setdefault(c, [])
                d[c].append(t)
                t = ''
            c = 0
        t += S[i]
    elif S[i] == 'ｗ':
        c += 1
if c > 0 and t != '':
    d.setdefault(c, [])
    d[c].append(t)

if d:
    print(*d[max(d)], sep='\n')
else:
    print('')
