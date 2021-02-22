n = int(input())
a = [int(input()) for _ in range(n - 1)]

result = 0
passengers = 0
for i in range(n - 1):
    b, c = map(int, input().split())
    passengers += c - b
    result += a[i] * passengers
print(result)
