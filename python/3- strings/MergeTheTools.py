def merge_the_tools(string, k):
    u, t = '', ''
    for i in string:
        t += i
        if i not in u:
            u += i
        if len(t) == k:
            print(u)
            t = u = ''
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)