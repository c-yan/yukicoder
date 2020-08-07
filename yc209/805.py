N = int(input())
S = input()

result = 0
i = -1
while i < N:
    i = S.find('U', i + 1)
    if i == -1:
        break
    j = i
    while j < N:
        j = S.find('M', j + 1)
        if j == -1:
            break
        k = 2 * j - i
        if k < N and S[k] == 'G':
            result += 1
print(result)
