N = int(input())

members = N * (1000000 // 10000)
wrong = (1000000 - members) * 1
arestees = wrong + members * 99

print(100 * wrong / arestees)
