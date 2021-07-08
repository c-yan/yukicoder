N = int(input())

for i in range(1, 10 ** 6 + 1):
    if i ** 3 == N:
        print('Yes')
        break
else:
    print('No')
