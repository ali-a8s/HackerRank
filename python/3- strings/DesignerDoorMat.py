h, w = input().split()
h = int(h)
w = int(w)

for i in range(w):
    i += 1
    if i <= h//2:
        print((".|." * (2*i-1)).center(w, "-"))

print(("WELCOME").center(w, "-"))

for i in range(w, 0, -1):
    if i <= h//2:
        print((".|." * (2*i - 1)).center(w, "-"))