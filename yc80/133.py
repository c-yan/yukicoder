from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

wins = 0
games = 0
for a in permutations(A):
    for b in permutations(B):
        games += 1
        t = 0
        for i in range(N):
            if a[i] > b[i]:
                t += 1
        if t > N // 2:
            wins += 1
print(wins / games)
