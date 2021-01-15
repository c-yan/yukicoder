A = input()
S = input()

result = ''
for c in S:
    if c in '0123456789':
        result += A[int(c)]
    else:
        result += c
print(result)
