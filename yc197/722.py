A, B = map(int, input().split())

t = A
n = 0
while t != 0 and t % 10 == 0:
    t //= 10
    n += 1
a = t

t = B
m = 0
while t != 0 and t % 10 == 0:
    t //= 10
    m += 1
b = t

if 1 <= abs(a) <= 9 and n >= 2 and 1 <= abs(b) <= 9 and m >= 2:
    print(A * B // 10)
else:
    if -99999999 <= A * B <= 99999999:
        print(A * B)
    else:
        print('E')
