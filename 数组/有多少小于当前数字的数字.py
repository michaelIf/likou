# 1365
# 双for循环
# author jh
def smallerNumbersThanCurrent(nums):
    res = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] > nums[j] and j != i:
                count += 1
        res.append(count)
    return res

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))

# 计数排序
# author 大梦三千秋
def way2(nums):
    count = [0] * 101
    n = len(nums)
    res = []
    for i in range(n):
        count[nums[i]] += 1

    for i in range(1, 101):
        count[i] += count[i - 1]

    for i in range(n):
        num = count[nums[i] - 1] if nums[i] else 0
        res.append(num)
    return res

# 直接排序后取index
# author 猫
def way3(nums):
    temp =  sorted(nums)
    res = []
    for n in nums:
        res.append(temp.index(n))
    return res