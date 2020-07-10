N, *T = map(int, open(0).read().split())

x = [0, 2, 4, 5, 7, 9, 11]

result = -1
for i in range(12):
    t = set((i + e) % 12 for e in x)
    for e in T:
        if e not in t:
            break
    else:
        if result == -1:
            result = i
        else:
            print(-1)
            exit()
print(result)
