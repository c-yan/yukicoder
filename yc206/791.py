N = int(input())

if N < 13:
    print('-1')
    exit()

i = 0
while N >= 10:
    if N % 10 != 3:
        print('-1')
        exit()
    N //= 10
    i += 1

if N != 1:
    print('-1')
else:
    print(i)
