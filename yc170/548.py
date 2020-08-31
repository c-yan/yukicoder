S = input()

d = {}
for c in 'abcdefghijklm':
    d[c] = 0
for c in S:
    d[c] += 1

if max(d.values()) >= 3:
    print('Impossible')
elif list(d.values()).count(2) >= 2:
    print('Impossible')
elif list(d.values()).count(2) == 1:
    print([k for k in d if d[k] == 0][0])
else:
    print(*'abcdefghijklm', sep='\n')
