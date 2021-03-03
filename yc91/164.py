N = int(input())

result = 10 ** 19
for _ in range(N):
    V = input()
    r = 0
    for c in V:
        if c in '0123456789':
            r = max(r, int(c) + 1)
        else:
            r = max(r, ord(c) - ord('A') + 11)
    result = min(result, int(V, r))
print(result)
