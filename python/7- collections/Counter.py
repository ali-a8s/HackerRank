from collections import Counter

X = int(input()) 
shoe_stock = Counter(list(map(int,input().split(" "))))
num_of_customers = int(input())
earned = 0

for i in range(num_of_customers):
    cust_size, cust_price = list(map(int,input().split(" ")))
    if shoe_stock[cust_size]:
        shoe_stock[cust_size] -= 1
        earned += cust_price

print(earned)