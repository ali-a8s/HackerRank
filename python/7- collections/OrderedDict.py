from collections import OrderedDict

n = int(input())
ItemPriceDic = OrderedDict()

for _ in range(n):
    Inp = input().split()
    item_name = ' '.join(Inp[:-1])
    item_price = int(Inp[-1])
    if item_name in ItemPriceDic.keys():
        ItemPriceDic[item_name] += item_price
    else:
        ItemPriceDic[item_name] = item_price
        
for i in ItemPriceDic:
    print(' '.join(map(str,(i,ItemPriceDic[i]))))
