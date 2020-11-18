# 哈希表
def findDisappearedNumbers(nums):
    hash_table = {}
    for num in nums:
        hash_table[num] = 1
    res = []
    for num in range(1, len(nums) + 1):
        if num not in hash_table:
            res.append(num)
    return res


# 原地修改
def way2(nums):
    for i in range(len(nums)):
        new_index = abs(nums[i]) - 1
        if nums[new_index] > 0:
            nums[new_index] *= -1
    res = []
    for i in range(1, len(nums) + 1):
        if nums[i - 1] > 0:
            res.append(i)
    return res


def findDisappearedNumbers2(self, nums):
    for i in range(len(nums)):
        new_index = abs(nums[i]) - 1
        if nums[new_index] > 0:
            nums[new_index] *= -1
    result = []
    for i in range(1, len(nums) + 1):
        if nums[i - 1] > 0:
            result.append(i)
    return result


