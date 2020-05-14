N = int(input())
M = int(input())

if N % 2 == 0:
    if M % 2 == 0:
        print('Yes')
    else:
        print('No')
else:
    if M >= 10 and M % 2 == 0:
        print('Yes')
    else:
        print('No')
