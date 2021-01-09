# 509
# 递归
# author jh
def fib(n):
    if n < 2:
        return n

    else:
        return fib(n-1) + fib(n-2)


# 动态规划
# author official
def way2(n):
    if n < 2:
        return n
    p, q, r = 0, 0, 1
    for i in range(2, n + 1):
        p, q = q, r
        r = p + q
    return r
