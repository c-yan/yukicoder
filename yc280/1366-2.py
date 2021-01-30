def is_kadomatsu(a):
    if a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
        return False
    return min(a) == a[1] or max(a) == a[1]


a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(3):
    for j in range(3):
        a[i], b[j] = b[j], a[i]
        if is_kadomatsu(a) and is_kadomatsu(b):
            print('Yes')
            exit()
        a[i], b[j] = b[j], a[i]
print('No')
