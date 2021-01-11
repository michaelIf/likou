# 1200
# 先排序，再找到最小值，再将结果保存到列表
def minimumAbsDifference(arr):
    arr.sort()
    temp = arr[1] - arr[0]
    res = []
    for i in range(1, len(arr)-1):
        if arr[i+1] - arr[i] < temp:
            temp = arr[i+1] - arr[i]
    for j in range(0, len(arr) - 1):
        if arr[j+1] - arr[j] == temp:
            res.append([arr[j], arr[j+1]])
    return res
arr = [1,3,6,10,15]
print(minimumAbsDifference(arr))
