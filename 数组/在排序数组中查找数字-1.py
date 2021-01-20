# 剑指 Offer 53 - I
# 使用字典
# author jh
def search(nums, target):
    import collections
    dd = collections.Counter(nums)
    for i, j in dd.items():
        if i == target:
            return j
    return 0



#
def way2(nums, target):
    i, j = 0, len(nums) - 1
    # 右边界
    while i <= j:
        m = (i + j)//2
        if nums[m] <= target:
            i = m + 1
        else:
            j = m - 1
    right = i
    if j >= 0 and nums[j] != target:
        return 0
    # 左边界
    i = 0
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        else:
            j = m - 1
    left = j
    return right - left - 1



#
def way3(nums, target):
    def helper(tar):
        i, j = 0, len(nums)-1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= tar:
                i = m + 1
            else:
                j = m - 1
        return i
    return helper(target) - helper(target-1)


