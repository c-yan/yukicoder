S, T, c = input().split()

S = int(S)
T = int(T)

if c == '<':
    result = S < T
elif c == '>':
    result = S > T
elif c == '=':
    result = S == T

if result:
    print('YES')
else:
    print('NO')
