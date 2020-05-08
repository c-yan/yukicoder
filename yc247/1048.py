L, R, M, K = map(int, input().split())

if R * K // M * M >= L * K:
    print('Yes')
else:
    print('No')
