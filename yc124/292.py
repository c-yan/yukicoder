S, t, u = input().split()
t = int(t)
u = int(u)

print(''.join(S[i] for i in range(len(S)) if i != t and i != u))
