def count_substring(string, sub_string):
    idx = string.find(sub_string)
    if idx == -1:
        return 0
    else:
        return 1 + count_substring(string[(idx + 1):], sub_string)
        
        
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)