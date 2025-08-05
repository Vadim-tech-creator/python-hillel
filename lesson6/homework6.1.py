import string

a, b = input().split('-')
abc = tuple(string.ascii_letters)
i = abc.index(a)
j = abc.index(b)
for c in abc[i:j+1]:
    print(c, end='')