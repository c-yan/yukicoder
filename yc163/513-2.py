def query(x, y):
    print(x, y)
    result = int(input())
    if result == 0:
        exit()
    return result


a = query(0, 0)
b = query(100000, 0)
AX = (a - b + 100000) // 2
AY = a - AX
query(AX, AY)
