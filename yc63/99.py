N, *X = map(int, open(0).read().split())

evens = 0
odds = 0
for x in X:
    if x % 2 == 0:
        evens +=1
    elif x % 2 == 1:
        odds += 1
print(abs(evens - odds))
