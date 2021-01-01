# 985
# 超出时间限制
# author jh
def sumEvenAfterQueries(A, queries):
    le_q = len(queries)
    ans = []
    for i in range(le_q):
        A[queries[i][1]] = A[queries[i][1]] + queries[i][0]
        temp = 0
        for j in A:
            if j % 2 == 0:
                temp += j
        ans.append(temp)
    return ans
A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
# print(sumEvenAfterQueries(A, queries))

def way2(A, queries):
    S = sum(x for x in A if x % 2 == 0)
    ans = []
    for x, k in queries:
        if A[k] % 2 == 0:
            S -= A[k]
        A[k] += x
        if A[k] % 2 == 0:
            S += A[k]
        ans.append(S)
    return ans
print(way2(A, queries))














