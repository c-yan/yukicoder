X = input()

if len(set(X)) == 1:
    print(-1)
    exit()

t = sorted(X, reverse=True)
Y1 = ''.join(t)

for i in range(len(t) - 2, -1, -1):
    if t[i] != t[len(t) - 1]:
        break

a, b = t[i], t[i + 1]
t[i], t[i + 1] = b, a
Y2 = ''.join(t)

if Y2[0] == '0':
    print(-1)
else:
    print(Y2)
