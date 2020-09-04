n, m = map(int, input().split())

if m >= n:
    print(1)
elif n % 2 == 0 and m >= n //  2:
    print(2)
else:
    print(-1)
