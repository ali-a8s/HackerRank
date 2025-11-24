from itertools import groupby

a = input()
b = [int(i) for i in a]

for x, y in groupby(b):
    n = len(list(y))
    print((n, x), end=" ")