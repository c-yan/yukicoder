X, N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = X in A
b = X in B
if a and b:
    print('MrMaxValu')
elif a:
    print('MrMax')
elif b:
    print('MaxValu')
else:
    print(-1)
