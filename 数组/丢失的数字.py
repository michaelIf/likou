# 268
# author jh
def missingNumber(nums):
    for i in range(len(nums) + 1):
        if i not in nums:
            return i

# 数学方法--0-n 的总和为n(n+1)/2,用其减去nums中数字总和，即可得到结果
# author official
def way2(nums):
    s1 = len(nums)*(len(nums)+1) // 2
    s2 = sum(nums)
    return s1 - s2