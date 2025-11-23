# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

i = m_set.intersection(n_set)

print(len(i))