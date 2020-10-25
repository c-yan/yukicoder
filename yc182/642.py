N = int(input())

result = 0
while N != 1:
    if N & 1 == 1:
        N += 1
        result += 1
    N >>= 1
    result += 1
print(result)
