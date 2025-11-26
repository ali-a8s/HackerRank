import re

def solve(regex):
    try:
        if re.search(r'(\*|\+|\?){2,}', regex):
            return False
        re.compile(regex)
        return True
    except re.error:
        return False
    

n = int(input())

for _ in range(n):
    regex = input()
    print(solve(regex))