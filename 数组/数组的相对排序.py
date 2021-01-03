# 1122
# author jh
def relativeSortArray(arr1, arr2):
    res = []
    temp = []
    for m in arr1:
        if m not in arr2:
            temp.append(m)
    for i in arr2:
        for j in range(len(arr1)):
            if arr1[j] == i:
                res.append(i)
    temp.sort()
    return res + temp

# 自定义排序
# author official
def way3(arr1, arr2):
    def mycmp(x):
        return (0, rank[x]) if x in rank else (1, x)
    rank = {x: i for i, x in enumerate(arr2)}
    arr1.sort(key=mycmp)
    return arr1

# 计数排序
def way2(arr1, arr2):
    upper = max(arr1)
    fre = [0] * (upper + 1)
    for x in arr1:
        fre[x] += 1
    ans = list()
    for x in arr2:
        ans.extend([x] * fre[x])
        fre[x] = 0
    for x in range(upper + 1):
        if fre[x] > 0:
            ans.extend([x] * fre[x])
    return ans


