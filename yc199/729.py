S = input()
i, j = map(int, input().split())

t = list(S)
a, b = t[i], t[j]
t[i], t[j] = b, a
print(''.join(t))
