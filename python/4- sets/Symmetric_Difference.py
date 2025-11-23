m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

sd = m_set.symmetric_difference(n_set)

print(len(sd))