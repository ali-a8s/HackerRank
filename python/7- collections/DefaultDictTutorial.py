from collections import defaultdict

n, m = map(int, input().split())
group_a = defaultdict(list)

for i in range(n):
    group_a[input()].append(i+1)

for i in range(m):
    word = input()
    if word in group_a.keys():
        print(*group_a[word], ' ')
    else:
        print('-1')