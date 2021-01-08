# 1652
# 循环数组，取余
# author Bollie
def decrypt(code, k):
    n = len(code)
    if k == 0: return [0] * n
    sign = 1 if k > 0 else -1
    res = [0] * n
    for i in range(n):
        for j in range(1, abs(k) + 1):
            res[i] += code[(n + i + j * sign) % n]
    return res


# 切片
'''
从给到的提示可以得知我们应该在3个code相加(列表相加)里面考虑，即原本的code前后各加一个code；
k=0时，直接返回len(code)个[0]列表相加；
k>0,k<0时，只需要遍历alist的中段(中间的code)即可，求和时注意切片的位置即可；
k<0时注意k是负数，负数，负数，负数
'''
# author luzzzzz
def way2(code, k):
    alist = code + code + code
    le = len(code)
    if k == 0:
        return [0] * le
    elif k > 0:
        return [sum(alist[x+1:x+k+1]) for x in range(le, len(alist)-le)]
    else:
        return [sum(alist[x + k:x]) for x in range(le, len(alist) - le)]

