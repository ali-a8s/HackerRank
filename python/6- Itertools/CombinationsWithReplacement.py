from itertools import combinations_with_replacement

a, b = input().split()
a = ''.join(sorted(a.upper()))

for i in combinations_with_replacement(a, int(b)):
    print(''.join(i))