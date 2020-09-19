N = int(input())

result = N * 2
while N != 0:
    result -= N
    N //= 2
print(result)
