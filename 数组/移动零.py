# 283
# 双for循环
# author jh
def moveZeroes(nums):
    for k in range(len(nums)):
        for i in range(len(nums) - 1):
            if nums[i] == 0 and nums[i + 1] != 0:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

# nums = [0,1,0,3,12]
# print(moveZeroes(nums))

# author jh
# 统计0的数量
def way2(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i-count] == 0:
            del nums[i-count]
            count += 1
            nums.append(0)
    return nums

nums = [0,0,1]
print(way2(nums))

# 双指针
# author official
def way3(nums):
    n = len(nums)
    left = right = 0
    while right < n:
        if nums[right] != 0:
            nums[left],nums[right] = nums[right], nums[left]
            left += 1
        right += 1

