# 219
# 双for循环, 超时
# author jh
def containsNearbyDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and j - i <= k:
                return True
    return False

# nums = [1,2,3,1]
# k = 3
# nums = [99,99]
# k = 2
# nums = [1,2,3,4,5,6,7,8,9,9]
# k = 3
nums = [1,2,3,1,2,3]
k = 2
# print(containsNearbyDuplicate(nums,k))

# 检查i,i+k区间
# 超时
# author jh
def way2(nums, k):
    if not nums:
        return False
    if len(nums) <= k:
        import collections
        dd = collections.Counter(nums)
        if max(dd.values()) >= 2:
            return True
    else:
        for i in range(len(nums) - k):
            for j in range(i + 1, i + k + 1):
                if nums[i] == nums[j]:
                    return True
        for m in range(len(nums)-k, len(nums)):
            for n in range(len(nums)-k, len(nums)):
                if nums[m] == nums[n] and abs(m-n) <= k and m!=n:
                    return True

    return False

# print(way2(nums,k))

# 使用字典记录index值
def way3(nums,k):
    d = {}
    for idx, n in enumerate(nums):
        if n not in d or (idx - d[n]) > k:
            d[n] = idx
        else:
            return True
    return False





