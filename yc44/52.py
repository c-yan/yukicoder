def f(s):
    if len(s) == 1:
        yield s
    else:
        for t in f(s[1:]):
            yield s[0] + t
        for t in f(s[:-1]):
            yield s[-1] + t


S = input()

print(len(set(f(S))))
