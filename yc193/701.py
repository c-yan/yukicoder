def conv(i):
    return ''.join(chr(ord('a') + int(c)) for c in str(i))


n = int(input())

result = []
for i in range(n - 1):
    result.append('a' + conv(i) + 'a')
result.append('a' + conv(n - 1) + 'n')
print(*result, sep='\n')
