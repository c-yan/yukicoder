N, M = map(int, input().split())
S = input()
T = input()

print(min(S.count('A'), T.count('A')) + min(S.count('B'), T.count('B')))
