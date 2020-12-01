# 暴力解法
def minSubsequence(nums):
    if len(nums) <= 1:
        return nums
    if len(nums) == 2 and nums[0] == nums[1]:
        return nums
    nums.sort()
    temp = 0
    ss = sum(nums)
    res = []
    for i in nums[::-1]:
        if temp > ss:
            return res
        else:
            temp += i
            ss -= i
            res.append(i)


#nums = [4,4,7,6,7]
# nums = [4,3,10,9,8]
# nums = [6]
nums = [8, 8]
print(minSubsequence(nums))

# 用后序和前序比较
def way2(nums):
    nums.sort()
    result = []
    while len(nums) > 0:
        result.append(nums.pop())
        if sum(result) > sum(nums):
            return result

