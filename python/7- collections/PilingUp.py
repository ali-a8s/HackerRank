for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    pair=[]
    midval=-1
    for i in range(len(s)//2):
        pair.append((s[i],s[-(i+1)]))
    flag="Yes"
    global_current=pair
    for i in range(1,len(pair)):
        prev=pair[i-1]
        curr=pair[i]
        if (curr[0]>prev[0] and  curr[0]>prev[1]) or (curr[1]>prev[0] and  curr[1]>prev[1]):
            flag="No"
            global_current=curr
    if len(s)%2==1 and flag=="Yes":
        midval=s[len(s)//2]
        if midval>global_current[0][0] and midval>global_current[0][1]:
            flag="No"
    print(flag)