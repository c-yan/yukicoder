r = ['%02X' % i for i in range(256)]
R = input()
if R != 'NONE':
    R = R.split(',')
    r = [e for e in r if all([x not in R for x in e])]

g = ['%02X' % i for i in range(256)]
G = input()
if G != 'NONE':
    G = G.split(',')
    g = [e for e in g if all([x not in G for x in e])]

b = ['%02X' % i for i in range(256)]
B = input()
if B != 'NONE':
    B = B.split(',')
    b = [e for e in b if all([x not in B for x in e])]

print(len(r) * len(g) * len(b))
