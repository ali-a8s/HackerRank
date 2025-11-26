from collections import deque

n= int(input())

d = deque()
for _ in range(n):
    command_line = input().split()
    command = command_line[0]
    arguments = command_line[1:]
    
    getattr(d, command)(*arguments)

print(*d)