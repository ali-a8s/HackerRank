students, subject = map(int, input().split())

X=[]

for _ in range(subject):
     X.append(list(map(float, input().split())))

scores = zip(*X)

for i in scores:
    print(sum(i)/subject)