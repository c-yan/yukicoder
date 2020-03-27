N = int(input())

t = [True] * 10
for _ in range(N):
    l = input().split()
    R = l[4]
    ABCD = list(map(int, l[:4]))
    if R == 'NO':
        for i in ABCD:
            t[i] = False
    elif R == 'YES':
        for i in set(range(10)) - set(ABCD):
            t[i] = False

for i in range(10):
    if not t[i]:
        continue
    print(i)
    break
