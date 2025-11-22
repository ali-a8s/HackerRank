if __name__ == '__main__':
    N = int(input())
    out = []
    for _ in range(N):
        parts = input().split()
        cmd = parts[0]
        args = list(map(int,parts[1:]))

        if cmd == 'print':
            print(out)
        else:
            getattr(out,cmd)(*args)