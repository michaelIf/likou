# 面试题08.03
# author jh
def findMagicIndex(nums):
    for i in range(len(nums)):
        if nums[i] == i:
            return i
    return -1

# 2分查找
# author kk.nike
def way2(nums):
    if not nums:
        return -1
    if nums[0] == 0:
        return 0
    p, n = 0, len(nums)
    while p < n:
        if nums[p] > p:
            p = nums[p]
        elif nums[p] == p:
            return p
        else:
            p += 1
    return -1
