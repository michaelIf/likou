# 1394
# author jh
def findLucky(arr):
    d = [0] * 500
    for i in arr:
        d[i] += 1
    for j in range(499, -1, -1):
        if j == d[j] and j != 0:
            return j
    return -1
arr = [2,2,3,4]
print(findLucky(arr))

# 使用字典
# author official
def way2(arr):
    res = -1
    d = dict()
    for i in arr:
        d[i] = d.get(i, 0) + 1
    for key, value in d.items():
        if key == value:
            res = max(res, key)
    return res