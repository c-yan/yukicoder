N = int(input())

if N == 0:
    print(0)
    exit()

s = ''
while len(s) < N:
    s += '142857'
print('0.' + s[:N])
