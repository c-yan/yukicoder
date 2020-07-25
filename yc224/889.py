N = int(input())

if N in [6, 28]:
    print('Kanzensu!')
elif N in [8, 27]:
    print('Ripposu!')
elif N in [4, 9, 16, 25, 36, 49]:
    print('Heihosu!')
elif N in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]:
    print('Sosu!')
else:
    print(N)
