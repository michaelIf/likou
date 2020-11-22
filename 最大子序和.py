# 暴力解法
def maxSubArray(nums):
    nums_length = len(nums)
    max_num = nums[0]
    for i in range(nums_length):
        temp = nums[i]
        for j in range(i+1, nums_length):
            max_num = max(max_num, temp)
            temp += nums[j]
        max_num = max(max_num, temp)
    return max_num


tt = [-2,1]
ss = maxSubArray(tt)
print(ss)
# 动态规划


def way2(nums):
    temp = 0
    max_num = nums[0]
    for i in nums:
        temp = max(temp + i, i)
        max_num = max(max_num, temp)
    return max_num

tt = [-2,1,2,3,5,-10,2]
ss = way2(tt)
print(ss)


# 动态规划2
def way3(nums):
    for i in range(1, len(nums)):
        nums[i] = max(nums[i-1] + nums[i], nums[i])
    return max(nums)