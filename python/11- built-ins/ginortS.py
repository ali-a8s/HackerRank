s = input()
upper = ""
lower = ""
odd = ""
even = ""
for i in sorted(s):
    if i.isupper():
        upper+=i
    elif i.islower():
        lower+=i
    elif int(i)%2==0:
        even+=i
    elif int(i)%2!=0:
        odd+=i
print(lower+upper+odd+even)