# 1588
# author jh
# 双for循环
def sumOddLengthSubarrays(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (j - i) % 2 == 0:
                temp = arr[i:j+1]
                res += sum(temp)
    return res
arr = [1,4,2,5,3]
print(sumOddLengthSubarrays(arr))

# author 认真的moon
# while 循环
def way2(arr):
    i, res = 1, 0
    while i <= len(arr):
        for j in range(len(arr) - i + 1):
            res += sum(arr[j: j + 1])
            i += 2
    return res






