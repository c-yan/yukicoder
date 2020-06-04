HA = int(input())
HB = int(input())
HC = int(input())

t = [(HA, 'A'), (HB, 'B'), (HC, 'C')]
t.sort(reverse=True)
for _, a in t:
    print(a)
