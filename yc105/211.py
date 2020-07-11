K = int(input())

t = 0
for i in [2,3,5,7,11,13]:
    for j in [4,6,8,9,10,12]:
        if i * j == K:
            t += 1
print(t / 36)
