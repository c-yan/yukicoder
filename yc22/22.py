N, K = map(int, input().split())
S = input()

p = K - 1
t = 0
while True:
    if S[p] == '(':
        t += 1
    elif S[p] == ')':
        t -= 1
    if t == 0:
        break
    if t > 0:
        p += 1
    elif t < 0:
        p -= 1
print(p + 1)
