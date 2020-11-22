N4 = input()

N = int(N4, 4)
if N % 15 == 0:
    print('FizzBuzz')
elif N % 3 == 0:
    print('Fizz')
elif N % 5 == 0:
    print('Buzz')
else:
    print(N4)
