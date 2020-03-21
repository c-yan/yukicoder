N = int(input())

if N == 1:
    print(1)
    exit()

result = ''
for i in range(N - 1, -1, -1):
    result += str(i) * N
print(result)
