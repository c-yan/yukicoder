N = int(input())

t = N % 360
if t == 90 or t == 270:
    print('Yes')
else:
    print('No')
