N = int(input())

if N == 0:
    print(0)
    exit()

t = ''
while N != 0:
    t += str(N % 7)
    N //= 7
print(t[::-1])
