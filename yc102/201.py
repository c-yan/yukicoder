SA, PA, XA = input().split()
SB, PB, XB = input().split()

PA = int(PA)
PB = int(PB)

if PA > PB:
    print(SA)
elif PA < PB:
    print(SB)
elif PA == PB:
    print(-1)
