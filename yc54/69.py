A = input()
B = input()

if ''.join(sorted(A)) == ''.join(sorted(B)):
    print('YES')
else:
    print('NO')
