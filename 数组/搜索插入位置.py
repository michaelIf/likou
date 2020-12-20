# 35
# author jh
def searchInsert(nums, target):
    if nums[-1] < target:
        return len(nums)
    for i, j in enumerate(nums):
        print(i,j)
        if j >= target:
            return i
# nums = [1,3,5,6]
# target = 5
# nums = [1,3,5,6]
# target = 0
nums = [1,3,5,6]
target = 7
# print(searchInsert(nums, target))
# 二分查找
# author jh
def way2(nums, target):
    if nums[-1] < target:
        return len(nums)
    left, right, ans = 0, len(nums)-1, 0
    while left <= right:

        mid = (right + left)//2
        if target <= nums[mid]:
            ans = mid
            right = mid -1
        else:
            left = mid + 1
    return ans

print(way2(nums, target))


# 二分模板
# author tinylife
def way3(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


