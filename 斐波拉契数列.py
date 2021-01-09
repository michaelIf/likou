def fb(n):
    if n <= 2:
        if n == 0:
            return 0
        return 1
    else:
        return fb(n-1) + fb(n-2)


def print_out(n):
    for i in range(1, n+1):
        ss = fb(i)
        print(ss)


print_out(9)




