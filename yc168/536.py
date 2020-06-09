S = input()

if S[-2:] == 'ai':
    print(S[:-2] + 'AI')
else:
    print(S + '-AI')
