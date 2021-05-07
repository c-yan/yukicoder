T = int(input())
for _ in range(T):
    s = input()
    t = s.split()
    t[2] = str(int(t[2]) + 1)
    print(' '.joint(t))
