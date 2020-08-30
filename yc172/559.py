S = input()

s = list(S)
result = 0
sorted = False
while not sorted:
    sorted = True
    for i in range(len(S) - 1):
        if s[i] > s[i + 1]:
            t = s[i]
            s[i] = s[i + 1]
            s[i + 1] = t
            result += 1
            sorted = False
print(result)
