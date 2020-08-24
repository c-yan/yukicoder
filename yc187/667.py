S = input()

o = S.count('o')
n = len(S)
for c in S:
    print(o * 100 / n)
    if c == 'o':
        o -= 1
    n -= 1
