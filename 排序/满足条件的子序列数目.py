# 排序+二分查找
def way2(nums, target):
    import bisect
    n = len(nums)
    P = 10**9 + 7
    f = [1] + [0] * (n-1)
    for i in range(1, n):
        f[i] = f[i-1] * 2 % P
    nums.sort()
    ans = 0
    for i, num in enumerate(nums):
        if nums[i] * 2 > target:
            break
        maxValue = target - nums[i]
        pos = bisect.bisect_right(nums, maxValue) - 1
        con = f[pos - i] if pos >= i else 0
        ans += con
    return ans % P
