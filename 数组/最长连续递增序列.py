# 674
# author jh

def findLengthOfLCIS(nums):
    n = len(nums)
    if n <= 1:
        return n
    count = 1
    i = 0
    li = []
    while i < n-1:
        if nums[i] < nums[i+1]:
            count += 1
            i += 1
        else:
            i += 1
            count = 1
        li.append(count)
    return max(li)

# print(findLengthOfLCIS(nums = [1]))

# 贪心
# author official
def way2(nums):
    n = len(nums)
    start = 0
    ans = 0
    for i in range(n):
        if i > 0 and nums[i] <= nums[i-1]:
            start = i
        ans = max(ans, i - start + 1)
    return ans
