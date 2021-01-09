# 1619
# author jh
def trimMean(arr):
    le = len(arr)
    count = round(le * 0.05, 0)
    count = int(count)
    arr.sort()
    temp = arr[count:le-count]
    res = sum(temp)/len(temp)
    return res

# arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
print(trimMean(arr))

# 取中间百分之90求平均
# author 天道妖星
def way2(arr):
    from numpy import mean
    arr.sort()
    return mean(arr[len(arr) // 20:len(arr) - len(arr) // 20])

