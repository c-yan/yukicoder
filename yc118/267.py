N = int(input())
mn = input().split()

def f(x):
    return 'DCHS'.index(x[0]) * 100 + 'A23456789TJQK'.index(x[1])

mn.sort(key=f)
print(*mn)
