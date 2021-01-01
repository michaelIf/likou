# 905
# author jh
def sortArrayByParity(A):
    even = []
    odd = []
    for i in A:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd

A = [3,1,2,4]
# print(sortArrayByParity(A))

# 按照模2的结果排序
# author official
def way2(A):
    A.sort(key=lambda x: x % 2)
    return A
print(way2(A))

# 快速排序
# author official
def way3(A):
    i, j = 0, len(A) - 1
    while i < j:
        if A[i] % 2 > A[j] % 2:
            A[i], A[j] = A[j], A[i]
        if A[i] % 2 == 0:
            i += 1
        if A[j] % 2 == 0:
            j -= 1
    return A


