N, K = map(int, input().split())

if N == K:
    print('Drew')
elif K == (N + 1) % 3:
    print('Won')
else:
    print('Lost')
