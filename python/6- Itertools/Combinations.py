from itertools import combinations


a, b = input().split()
a = sorted(list(a.upper()))
b = int(b)

s = []

for n in range(1, b+1):
    s.extend(sorted(list(combinations(a, n))))

for i in s:
    print(''.join(i))
