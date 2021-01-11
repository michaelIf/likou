# 剑指offer03
# 双for循环，超时
# author jh
def findRepeatNumber(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]

# 使用额外的列表
# author jh
def way2(nums):
    temp = []
    for i in nums:
        if i in temp:
            return i
        else:
            temp.append(i)

# 超时
# 切片
# author jh
def way3(nums):
    for i in range(len(nums)-1):
        if nums[i] in nums[i+1:]:
            return nums[i]


# 字典
# author jh
def way4(nums):
    d = {}
    for i in nums:
        if i in d:
            return i
        else:
            d[i] = 1

# 使用set
# author Krahets
def way5(nums):
    ss = set()
    for i in nums:
        if i in ss:
            return i
        ss.add(i)
    return -1

