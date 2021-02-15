N, K = map(int, input().split())
S = input()


def f(stock, S):
    pay = 0
    for c in S:
        if stock == 0:
            pay += 1
        else:
            stock -= 1
        stock += int(c)
    return pay, stock


if K <= N:
    print(f(0, S[:K])[0])
    exit()

pay, stock = f(0, S)

if stock >= pay:
    print(pay)
    exit()

print(pay + (pay - stock) * ((K - N) // N) + f(stock, S[:K % N])[0])
