# 10.01
# author jh
def merge(A, m, B, n):
    for i in range(n):
        A[m+i] = B[i]
    A.sort()
    return A

A = [1,2,3,0,0,0]
m = 3
B = [2,5,6]
n = 3
print(merge(A,m,B,n))

# 双指针
def way2(A, m, B, n):
    res = []
    pa, pb = 0, 0
    while pa < m or pb < n:
        if pa == m:
            res.append(B[pb])
            pb += 1
        elif pb == n:
            res.append(A[pa])
            pa += 1
        elif A[pa] < B[pb]:
            res.append(A[pa])
            pa += 1
        else:
            res.append(B[pb])
            pb += 1
    A[:] = res

# 逆向双指针
def way3(A, m, B, n):
    pa, pb = m - 1, n - 1
    tail = m+n-1
    while pa >= 0 or pb >= 0:
        if pa == -1:
            A[tail] = B[pb]
            pb -= 1
        elif pb == -1:
            A[tail] = A[pa]
            pa -= 1
        elif A[pa] > B[pb]:
            A[tail] = A[pa]
            pa -= 1
        else:
            A[tail] = B[pb]
            pb -= 1
        tail -= 1



