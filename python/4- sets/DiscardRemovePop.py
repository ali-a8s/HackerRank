n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input().split()
    
    if len(command) == 1:
        s.pop()
    elif len(command) == 2:
        if command[0] == 'remove':
            s.remove(int(command[1]))
        elif command[0] == 'discard':
            s.discard(int(command[1]))
            
print(sum(s))