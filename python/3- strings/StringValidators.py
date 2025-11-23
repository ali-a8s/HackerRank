if __name__ == '__main__':
    s = input()
    method_name = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']

    for name in method_name:
        print(any(getattr(c, name)() for c in s))