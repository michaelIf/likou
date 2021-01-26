# 1018
# 超出时间限制
# author jh
def prefixesDivBy5(A):
    res = []
    for i in range(1, len(A)+1):
        num = 0
        for k in range(i):
            num += A[k] * (2**(i-k-1))
        if num % 5 == 0:
            res.append(True)
        else:
            res.append(False)
    return res

# 位运算+模
def way2(A):
    res = []
    temp = 0
    for i in A:
        temp = ((temp << 1)+i) % 5
        res.append(temp == 0)
    return res




print(way2([0,1,1,1,1,1]))

ss = [0,1,3,7,15,31]

