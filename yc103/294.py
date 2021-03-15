D = int(input())
C = input() + input()

result = 0
for i in range(42):
    t = list(('o' * 14) + C + ('o' * 14))
    j = i
    while j < 42 and t[j] == 'o':
        j += 1
    c = 0
    while c < D and j < 42 and t[j] == 'x':
        t[j] = 'o'
        j += 1
        c += 1
    result = max(result, max(len(a) for a in ''.join(t).split('x')))
print(result)
