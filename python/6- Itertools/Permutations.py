from itertools import permutations

s,k = input().split()

for x in sorted(list(permutations(str(s),int(k)))): 
    print(''.join(x))