# 自己动手
def canMakeArithmeticProgression(arr):
    arr.sort()
    arr_le = len(arr)
    if arr_le <= 2:
        return False
    temp = arr[1] - arr[0]
    while arr_le-2:
        if arr[arr_le-1] - arr[arr_le-2] == temp:
            pass
        else:
            return False
        arr_le -= 1
    return True

# arr = [3,5,1]
arr = [1,2,4]
print(canMakeArithmeticProgression(arr))



# for 循环
def way2(arr):
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False
    return True

