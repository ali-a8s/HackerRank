from collections import Counter

n = int(input())
inp = []
for _ in range(n):
    inp.append(input())

inp_set = set(inp)
print(len(inp_set))

c = Counter(inp)
count = [count for item, count in c.items()]
print(*count, sep=' ')