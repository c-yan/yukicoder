A, B, C = map(int, input().split())

if B == 0:
    if C >= A or A == 0:
        print('Impossible')
    else:
        print(A - C)
else:
    if C >= A + B + 10:
        print('Impossible')
    elif C >= A + B:
        print(A + B + 9 - C)
    else:
        while A >= 10 and (A - 10) + (B + 1) > C:
            B += 1
            A -= 10
        if A + B - C <= A:
            print(A + B - C)
        else:
            print((B - C) * 10 + A)
