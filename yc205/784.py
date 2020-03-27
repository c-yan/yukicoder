N = int(input())

t = str(N)[::-1]
a = []
for i in range(0, len(t), 3):
    a.append(t[i:i+3])
print(','.join(a)[::-1])
