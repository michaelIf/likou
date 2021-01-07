# 1304
# 从两边取值，分别为+-相同的数
# author jh
def sumZero(n):
    res = []
    if n == 0:
        return [0]
    if n % 2 == 0:
        for i in range(1, n//2+1):
            res.extend([i, -i])
    else:
        for i in range(1, n//2+1):
            res.extend([i, -i])
        res.append(0)
    return res
print(sumZero(0))

# author official
# 将 n-1个数放入数组，和为sum，再加入一个-sum即可
def way2(n):
    ans = [x for x in range(n-1)]
    ans.append(-sum(ans))
    return ans
