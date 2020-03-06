S = input()
T = input()

if len(T) == 1:
    if S.find(T) == -1:
        print(0)
    else:
        print(-1)
    exit()

result = 0
p = 0
while True:
    p = S.find(T, p)
    if p == -1:
        break
    p += len(T) - 1
    result += 1
print(result)
