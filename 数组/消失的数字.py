# 面试题17.04
# author jh
# 另类if else
def missingNumber(nums):
    n = len(nums)
    nums.sort()
    for i in range(n):
        if i != nums[i]:
            return i
    else:
        return n
