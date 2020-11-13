# 先找到奇数和偶数，再利用zip
def sortArrayByParityII(A):
    import itertools
    res_odd = []
    res_even = []
    res = []
    for i in A:
        if i % 2 == 0:
            res_even.append(i)
        else:
            res_odd.append(i)
    res = list(itertools.chain.from_iterable(zip(res_even, res_odd)))


    return res


A = [4,2,5,7]

ss = sortArrayByParityII(A)
print(ss)

# 一次遍历
def way2(A):
    B = [-1] * len(A)
    even = 0
    odd = 1
    for i in A:
        if i % 2 == 0:
            B[even] = i
            even += 2
        else:
            B[odd] = i
            odd += 2
    return B
A = [4,2,5,7]

ss = sortArrayByParityII(A)
print(ss)

# 双指针
def way3(A):
    pass


