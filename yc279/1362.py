from collections import Counter

S = input()

c = Counter(S)
a = [k for k in c if c[k] == 1][0]
print(S.index(a) + 1, a)
