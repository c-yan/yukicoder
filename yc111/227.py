A = list(map(int, input().split()))

d = {}
for a in A:
    d.setdefault(a, 0)
    d[a] += 1

if len(d) == 2 and sorted(d.values()) == [2, 3]:
    print('FULL HOUSE')
elif 3 in d.values():
    print('THREE CARD')
elif len(d) == 3 and sorted(d.values()) == [1, 2, 2]:
    print('TWO PAIR')
elif 2 in d.values():
    print('ONE PAIR')
else:
    print('NO HAND')
