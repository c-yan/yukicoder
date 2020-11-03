N = int(input())
S = input()

result = [None] * N
t = [None] * (N // 2)
c = 0
for i in range(N):
    if S[i] == '(':
        t[c] = i + 1
        c += 1
    elif S[i] == ')':
        c -= 1
        result[t[c] - 1] = i + 1
        result[i] = t[c]
print(*result, sep='\n')
