from collections import Counter

G, C, P = map(int, input().split())
S = input()

c = Counter(S)
c.setdefault('G', 0)
c.setdefault('C', 0)
c.setdefault('P', 0)

result = 0

a = min(G, c['C'])
result += 3 * a
G -= a
c['C'] -= a

a = min(C, c['P'])
result += 3 * a
C -= a
c['P'] -= a

a = min(P, c['G'])
result += 3 * a
P -= a
c['G'] -= a

a = min(G, c['G'])
result += a
G -= a
c['G'] -= a

a = min(C, c['C'])
result += a
C -= a
c['C'] -= a

a = min(P, c['P'])
result += a
P -= a
c['P'] -= a

print(result)
