from itertools import product

a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

res = list(product(a_lst, b_lst))

print(* res)