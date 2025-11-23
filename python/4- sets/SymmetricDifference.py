# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

for i in sorted(m_set ^ n_set):
    print(i)