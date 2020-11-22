# 暴力解法
def myPow(x, n):
    return x**n


# 快速幂+递归
def way2(x, n):
    def quickMu1(N):
        if N == 0:
            return 1.0
        y =quickMu1(N//2)
        return y*y if N % 2 == 0 else y*y*x
    return quickMu1(n) if n >= 0 else 1.0/quickMu1(-n)

tt  = way2(3, 2)
print(tt)

# 快速幂 + 迭代
def way3(x, n):
    def qiuckMu2(N):
        ans = 1.0
        x_con = x
        while N > 0:
            if N % 2 ==1:
                ans *= x_con
            x_con *= x_con
            N //= 2
        return ans
    return qiuckMu2(n) if n >=0 else 1.0 / qiuckMu2(-n)