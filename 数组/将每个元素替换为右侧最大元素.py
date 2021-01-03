# 1299
# author jh
def replaceElements(arr):
    res = []
    for i in range(len(arr)):
        temp = arr[i+1:len(arr)]
        if not temp:
            res.append(-1)
            break
        if arr[i+1] > max(temp):
            res.append(arr[i])
        else:
            res.append(max(temp))
    return res

arr = [17,18,5,4,6,1]
# print(replaceElements(arr))

# 超时
# author jh
def way2(arr):
    le = len(arr)
    res = []
    ss = 0
    for i in range(le):
        if i == le-1:
            res.append(-1)
        else:
            max_num = arr[i + 1]
            for j in range(i + 1, le):
                if arr[j] > max_num:
                    max_num = arr[j]
            res.append(max_num)
    return res
print(way2(arr))

# 逆序遍历
# author official
def way3(arr):
    n = len(arr)
    ans = [0] * (n-1) + [-1]
    for i in range(n-2, -1, -1):
        ans[i] = max(ans[i+1], arr[i + 1])
    return ans