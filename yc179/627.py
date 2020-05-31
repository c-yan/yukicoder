T = int(input())
x = 0
for _ in range(T):
    X = int(input())
    if x + 1 != X and x -1 != X:
        print('F')
        exit()
    x = X
print('T')
