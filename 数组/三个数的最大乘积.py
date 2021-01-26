# 628
# author jh
def maximumProduct(nums):
    if len(nums) <= 2:
        return False
    if len(nums) == 3:
        return nums[0]*nums[1]*nums[2]
    nums.sort()
    if nums[1] >= 0:
        return nums[-1]*nums[-2]*nums[-3]
    else:
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

# 找到3个最大的数和2个最小的数
def way2(nums):
    a = b = c = float('inf')
    d = e = float('inf')
    for i, num in enumerate(nums):
        if num > a:
            a, b, c = num, a, b
        elif num > b:
            b, c = num, b
        elif num > c:
            c = num
        if num < d:
            d, e = num, d
        elif num < e:
            e = num
    return max(d*e*a, a*b*c)
