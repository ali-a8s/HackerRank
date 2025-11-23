def average(array):
    # your code goes here
    arr = set(array)
    res = sum(arr) / len(arr)
    return res
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)