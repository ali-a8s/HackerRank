def print_rangoli(size):
    charList = []
    myPattern = []
    for a in range(size):
        charList.append(chr(97 + a))
    charList.reverse()
    columns = (2 * len(charList))-1
    columns = (2 * columns) - 1
    for iteration in range(len(charList)):
        charsNum = iteration+1
        currentChar = charList[:charsNum]
        reversed_list = currentChar[::-1]
        ascending_part = reversed_list[1:]
        reversed_list.reverse()
        full_pattern_list = reversed_list + ascending_part
        myPattern.append("-".join(full_pattern_list))
    for item in myPattern:
        print(item.center(columns,'-'))
    length = len(myPattern)
    for item in reversed(myPattern):
        if item is not myPattern[length-1]:
            print(item.center(columns,'-'))

      
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)