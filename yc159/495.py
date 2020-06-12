S = input()

t = 0
for i in range(0, len(S), 5):
    if S[i:i + 5] == '(^^*)':
        t += 1

print(t, len(S) // 5 - t)
