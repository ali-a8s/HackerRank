t = int(input())

for _ in range(t):
    for i  in ['a', 'b']:
        exec(f'{i} = int(input())')
        exec(f'{i}_arr = set(map(int, input().split()))')
        
    print(a_arr.issubset(b_arr))