n, *a = map(int, open(0).read().split())

for i in range(1, 2 * n - 3):
    for p in range(max(i - n + 1, 0), n - 2):
        q = i - p
        if p >= q:
            break
        if a[p] <= a[q]:
            continue
        t = a[p]
        a[p] = a[q]
        a[q] = t
print(*a)
