# 滴滴面试题 2021.01.15
'''
给定一个数组int[]，int[i]>0  
求：每个元素后面第一个值比它大的数，如果没有，返回-1（时间复杂度最低）
Input [3, 1, 2, 4, 5]  
Output [4, 2, 4, 5, -1]
'''
# 双for循环
# author jh

def getBiggerNum(A):
    res = []
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] > A[i]:
                res.append(A[j])
                break
        else:
            res.append(-1)
    return res

A = [7, 3, 1, 2, 4, 6, 5]
# print(getBiggerNum(A))

# 使用单调栈
#
def way2(A):
    from  collections import deque
    if not A:
        return A
    stack = deque()
    stack.append(0)
    n = len(A)
    res = [0] * n
    index = 1
    while index < n:
        if stack and A[index] > A[stack[-1]]:
            res[stack.pop()] = A[index]
        else:
            stack.append(index)
            index += 1
    if stack:
        for i in stack:
            res[i] = -1


    return res

print(way2(A))


