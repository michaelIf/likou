# 21
# 深拷贝 + remove
# author jh
def removeElement(nums, val):
    from copy import deepcopy
    nums_d = deepcopy(nums)
    for k in nums_d:
        if k == val:
            nums.remove(k)
    print(nums)
    return len(nums)
nums = [3,2,2,3]
val = 3
# nums = [1,1,2,1,1,3,4]
# val = 1
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# print(removeElement(nums, val))

# 双指针
# author Flying_Du
def way2(nums, val):
    a = 0
    b = 0
    while a < len(nums):
        if nums[a] != val:
            nums[b] = nums[a]
            b += 1
        a += 1
    return b

# 倒序遍历
# author zhangxu_bme
def way3(nums, val):
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == val:
            nums.pop(i)
    return len(nums)












