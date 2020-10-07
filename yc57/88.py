S = input()
B = [input() for _ in range(8)]

if sum(b.count('.') for b in B) % 2 == 0:
    print(S)
else:
    print({"oda": "yukiko", "yukiko": "oda"}[S])
