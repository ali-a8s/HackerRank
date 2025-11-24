from itertools import combinations

N = int(input())
l = list(input().split())
n = int(input())

new = list(combinations(l, n))

count = 0

for i in new:
    if 'a' in i:
        count += 1


print(f"{count/len(new):.12f}")