# 896
# author jh
# 双for循环，超出时间限制
def isMonotonic(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[0] >= A[-1]:
                if A[i] < A[j]:
                    return False
            else:
                if A[i] > A[j]:
                    return False
    return True

A = [1,1,1]
# print(isMonotonic(A))

# while 循环
# author jh
def way2(A):
    right, left = 0, 1
    while left < len(A):
        if A[0] >= A[-1]:
            if A[left] > A[right]:
                return False
            left += 1
            right += 1
        else:
            if A[left] < A[right]:
                return False
            left += 1
            right += 1
    return True
# print(way2([1,1,1]))

# for循环一次
#
def way3(A):
    up = 1
    down = 1
    for i in range(1, len(A)):
        if not A[i-1] <= A[i]:
            up = 0
        if not A[i-1] >= A[i]:
            down = 0
    if up == 0 and down == 0:
        return False
    return True
print(way3([1,1,1]))
