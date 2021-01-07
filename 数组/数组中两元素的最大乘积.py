# 1464
# 双for循环
# author jh
def maxProduct(nums):
    res = (nums[0]-1) * (nums[1]-1)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] - 1) * (nums[j] - 1) > res:
                res = (nums[i] - 1) * (nums[j] - 1)
    return res

nums = [3,4,5,2]
print(maxProduct(nums))

# sort 取最后两位
# author jh
def way2(nums):
    nums.sort()
    return (nums[-1] - 1) * (nums[-2] - 1)

# 一次遍历取最大数和次大数
# author jerryluan
def way3(nums):
    f = s = 1
    for i in nums:
        if i > f:
            s = f
            f = i
        elif f >= i > s:
            s = i
    return (s-1) * (f-1)
