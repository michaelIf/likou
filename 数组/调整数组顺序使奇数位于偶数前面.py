# 剑指offer21
# author jh
def exchange(nums):
    left, right = 0, len(nums) - 1
    while right > left:
        if nums[left] % 2 == 1:
            left += 1
        else:
            if nums[right] % 2 == 0:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
    return nums

# author 孙琦
def way2(arr):
    m, n = 0, len(arr) - 1
    while m < n:
        if arr[m] % 2 == 0:
            arr[n], arr[m] = arr[m], arr[n]
            n -= 1
        else:
            m += 1
    return arr


def way3(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] % 2 == 1:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

ss = [6,2,3,4,7,8]
tt = way3(ss)
print(tt)


