def increment(S):
    carry = 1
    t = []
    for c in reversed(S):
        x = int(c) + carry
        if x == 10:
            t.append('0')
            carry = 1
        else:
            t.append(str(x))
            carry = 0
    if carry == 1:
        t.append('1')
    t = ''.join(reversed(t))
    if S[0] != '0':
        return t
    return S[:len(S)-len(t)] + t


def f(S):
    n = len(S)
    l, r = 0, 0
    for i in range(n):
        if r == 0 and S[n - 1 - i] in '0123456789':
            r = n - i
        elif r != 0 and S[n - 1 - i] not in '0123456789':
            l = n - i
            break
    if r == 0:
        return S
    return S[:l] + increment(S[l:r]) + S[r:]


T = int(input())
for _ in range(T):
    S = input()
    print(f(S))
