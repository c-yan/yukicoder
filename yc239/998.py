A, B, C, D = map(int, input().split())

t = [A, B, C, D]
t.sort()
for i in range(1, 4):
    if t[i - 1] + 1 == t[i]:
        continue
    print('No')
    exit()
print('Yes')
