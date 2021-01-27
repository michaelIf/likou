# 美餐网面试题
'''
在一个字符串数组中有红、黄、蓝三种颜色的球，且个数不相等、顺序不一致，请为该数组排序。
使得排序后数组中球的顺序为:黄、红、蓝
'''
def sort(arr):

    red = []
    yellow = []
    blue = []
    for i in arr:
        if i == "红":
            red.append(i)
        elif i == "黄":
            yellow.append(i)
        else:
            blue.append(i)
        return yellow + red + blue


temp = ['黄','红','黄','蓝','黄','蓝']
# print(sort(temp))

# 单指针
def way2(arr):
    p = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == '黄':
            arr[p], arr[i] = arr[i], arr[p]
            p += 1
    for j in range(p, n):
        if arr[j] == '红':
            arr[p], arr[j] = arr[j], arr[p]
    return arr

# print(way2(temp))

# 双指针
def way3(arr):
    n = len(arr)
    p0 = p1 = 0
    for i in range(n):
        if arr[i] == '红':
            arr[i], arr[p1] = arr[p1], arr[i]
            p1 += 1
        elif arr[i] == '黄':
            arr[i], arr[p0] = arr[p0], arr[i]
            if p0 < p1:
                arr[i], arr[p1] = arr[p1], arr[i]
            p1 += 1
            p0 += 1
    return arr
# print(way3(temp))

# 双指针2
def way4(arr):
    n = len(arr)
    p0, p2 = 0, n-1
    i = 0
    while i < p2:
        while i <= p2 and arr[i] == '蓝':
            arr[i], arr[p2] = arr[p2], arr[i]
            p2 -= 1
        if arr[i] == '黄':
            arr[i], arr[p0] = arr[p0], arr[i]
            p0 += 1
        i += 1
    return arr

# print(way4(temp))

# 三指针
def way5(arr):
    r, w, b = 0, 0, len(arr) - 1
    while w <= b:
        if arr[w] == '黄':
            arr[r], arr[w] = arr[w], arr[r]
            r += 1
            w += 1
        elif arr[w] == '红':
            w += 1
        else:
            arr[w], arr[b] = arr[b], arr[w]
            b -= 1
    return arr
# print(way5(temp))

def way6(arr):
    def swap(arr, index1, index2):
        arr[index1], arr[index2] = arr[index2], arr[index1]
    ye = 0
    bl = len(arr)
    i = 0
    while i < bl:
        if arr[i] == '黄':
            swap(arr, i, ye)
            i += 1
            ye += 1
        elif arr[i] == '红':
            i += 1
        else:
            bl -= 1
            swap(arr, i, bl)
    return arr
print(way6(temp))



