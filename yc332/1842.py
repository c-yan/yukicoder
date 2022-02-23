T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    print((A * pow(10, C, B * 10)) // B % 10)
