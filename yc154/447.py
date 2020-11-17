N = int(input())
L = list(map(int, input().split()))
T = int(input())

a = ''.join(chr(ord('A') + i) for i in range(N))

base_score = {}
acs = {}
for c in a:
    base_score[c] = L[ord(c) - ord('A')]
    acs[c] = 0

def score(c):
    acs[c] += 1
    return int(50 * base_score[c] + 50 * base_score[c] / (0.8 + 0.2 * acs[c]))

result = {}
for i in range(T):
    Name, P = input().split()
    if Name in result:
        s, _, r = result[Name]
    else:
        s = 0
        r = {}
    j = score(P)
    r[P] = j
    s += j
    result[Name] = [s, -i, r]

result = sorted(([result[k][0], result[k][1], k, result[k][2]] for k in result), reverse=True)
for i in range(len(result)):
    r = result[i]
    t = []
    t.append(i + 1)
    t.append(r[2])
    for c in a:
        if c in r[3]:
            t.append(r[3][c])
        else:
            t.append(0)
    t.append(r[0])
    print(*t)
