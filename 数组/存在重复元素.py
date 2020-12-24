# 217
# counter + 遍历
# author jh
def containsDuplicate(nums):
    import collections
    dd = collections.Counter(nums)
    for i in dd.values():
        if i >= 2:
            return True
    return False

# 使用额外的列表
# 超时
# author jh
def way2(nums):
    temp = []
    for i in nums:
        if i in temp:
            return True
        else:
            temp.append(i)
    return False

# 排序
# author official
def way3(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return False