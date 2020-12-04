def findLeastNumOfUniqueInts(arr, k):
    tmp_dict = {}
    for i in arr:
        if i in tmp_dict:
            tmp_dict[i] += 1
        else:
            tmp_dict[i] = 1
    res = sorted(tmp_dict.items(), key=lambda x: (x[1]))
    temp = 0
    for i, j in enumerate(res):
        temp += res[i][1]
        if temp == k:
            return len(res)-i-1
        elif temp > k:
            return len(res)-i
        else:
            continue


# arr = [5,5,4]
# k = 1
arr = [4,3,1,1,3,3,2]
k = 3
print(findLeastNumOfUniqueInts(arr,k))

# 计数排序和贪心算法
def way2(arr, k):
    from collections import Counter
    arr_count = Counter(arr)
    print(arr_count)
    arr_count = sorted(arr_count.items(), key=lambda item: item[1])
    print(arr_count)
    tmp = arr_count[:]
    print(tmp)
    for item_count in arr_count:
        if item_count[1] <= k:
            tmp.remove(item_count)
            k -= item_count[1]
    return len(tmp)
arr = [4,3,1,1,3,3,2]
k = 3
print(way2(arr,k))

# 最快的方法
def way3(arr, k):
    from collections import Counter
    count = Counter(arr)
    sortv = sorted(count.values())
    for ind, ele in enumerate(sortv):
        k -= ele
        if k == 0:
            return len(sortv) - (ind + 1)
        elif k < 0:
            return len(sortv) - ind
    return 0



