A = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    B = set(map(int, input().split()))
    
    if(not(A > B)):
        print(False)
        break
else:
    print(True)