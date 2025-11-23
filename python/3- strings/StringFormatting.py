def print_formatted(number):
    number_bin = f"{number:b}"
    width = len(number_bin)
    for i in range(1, number + 1):
        result = f"{i}".rjust(width)+ " " + f"{i:o}".rjust(width) + " " + f"{i:X}".rjust(width)+ " " + f"{i:b}".rjust(width)
        print(result)
        
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)