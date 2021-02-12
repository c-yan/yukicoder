m = 1000000007

N = int(input())

t = []
a = N
while a != 0:
    t.append(a % 2)
    a //= 2

result = 0
a = 3
b = 10
for i in range(len(t)):
    if t[i] == 1:
        result = (result * b) + a
        result %= m
    a = a * b + a
    a %= m
    b *= b
    b %= m
result += pow(10, N, m)
result %= m
print(result)
