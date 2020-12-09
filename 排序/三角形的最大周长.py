# 976
# while 循环
def largestPerimeter(A):
    A.sort(reverse=True)
    le = len(A)
    i = 0
    while le - 2 > i:
        if A[i] < A[i + 1] + A[i + 2]:
            return A[i] + A[i + 1] + A[i + 2]
        else:
            i += 1
    return 0

# A = [2,1,2]
A = [1,2,1]
print(largestPerimeter(A))

# for循环
def way2(A):
    A.sort(reverse=True)
    le = len(A)
    for i in range(le-2):
        if A[i] < A[i + 1] + A[i + 2]:
            return A[i] + A[i + 1] + A[i + 2]
        else:
            i += 1
    return 0

A = [2,1,2]
# A = [1,2,1]
print(way2(A))



