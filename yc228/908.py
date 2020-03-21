S = input()

if all(c == ' ' for c in S[1::2]) and all('a' <= c <= 'z' for c in S[::2]):
    print('Yes')
else:
    print('No')
