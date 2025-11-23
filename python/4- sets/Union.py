m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

u = m_set.union(n_set)

print(len(u))