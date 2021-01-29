S = input()

i = 0
for c in S:
    j = 'kadomatsu'.find(c, i)
    if j == -1:
        print('No')
        break
    i = j + 1
else:
    print('Yes')
