# 美团面试题
'''
in [2,-2,5,-1,4,-5]
out [2,5,4,-2,-1,-5]
'''
def sort(arr):
    res = []
    temp = []
    for i in arr:
        if i > 0:
            res.append(i)
        else:
            temp.append(i)
    return res + temp

# 不使用额外的空间
def way2(arr):
    left, right = 0, 1

    while left < len(arr):
        if arr[left] < 0:
            if arr[right] > 0:
                arr[right], arr[left] = arr[left], arr[right]
            else:
                if right < len(arr)-1:
                    right += 1
                else:
                    break
        else:
            left += 1

    return arr
ss = [2,-2,5,-1,4,-5]
print(way2(ss))


