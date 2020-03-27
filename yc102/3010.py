from os import listdir

for s in sorted(listdir('/bin')):
    if s[0] == '.':
        continue
    print(s)
