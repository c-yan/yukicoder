S = input()

result = -1
i = S.find('c')
while i != -1:
    j = S.find('w', i + 1)
    if j == -1:
        break
    k = S.find('w', j + 1)
    if k == -1:
        break
    if result == -1:
        result = k - i + 1
    else:
        result = min(result, k - i + 1)
    i = S.find('c', i + 1)
print(result)
