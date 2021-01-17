# 1287
# 使用字典
# author jh
def findSpecialInteger(arr):
    import collections
    dd = collections.Counter(arr)
    tt = sorted(dd.items(), key=lambda x: x[1])
    return tt[-1][0]

arr = [1,2,2,6,6,6,6,7,10]
# print(findSpecialInteger(arr))


# author jh
def way2(arr):
    le = len(arr)
    if le == 1:
        return arr[0]
    ss = le // 4
    tt = le % 4
    if tt > 0:
        ss += 1
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        if d[i] > ss:
            return i
print(way2(arr))

# author official
# 遍历
def way3(arr):
    n = len(arr)
    cur, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == cur:
            cnt += 1
            if cnt * 4 > n:
                return cur
        else:
            cur, cnt = arr[i], 1
    return -1
