def frog(n):
    if n <= 2:
        return n
    else:
        return frog(n-1) + frog(n-2)


def print_step(n):
    for i in range(1, n+1):
        print(frog(i))


print_step(4)

