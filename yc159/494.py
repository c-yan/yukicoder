S = input()

for i in range(len(S)):
    if S[i] != '?':
        continue
    print('yukicoder'[i])
    break
