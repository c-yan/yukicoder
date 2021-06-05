N = int(input())

if N in [1, 2]:
    print(1)
elif N in [3, 5]:
    print(-1)
elif N == 4:
    print(2, 4)
else:
    t = [2, 4]
    for i in range(8, N + 1, 2):
        t.append(i)
    t.append(6)
    if N % 2 == 1:
        t.append(3)
    print(*t)
