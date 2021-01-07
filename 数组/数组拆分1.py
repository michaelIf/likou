# 561
# author
def arrayPairSum(nums):
    nums.sort()
    res = 0
    for i in range(len(nums)//2):
        res += nums[2*i]
    return res
nums = [1,4,3,2]
print(arrayPairSum(nums))

# 一行
def way2(nums):
    return sum(sorted(nums)[::2])