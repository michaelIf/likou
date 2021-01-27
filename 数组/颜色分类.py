# 75
# author official

# 单指针
def sortColors(nums):
    n = len(nums)
    ptr = 0
    for i in range(n):
        if nums[i] == 0:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    for j in range(ptr, n):
        if nums[j] == 1:
            nums[j], nums[ptr] = nums[ptr], nums[j]
            ptr += 1

# 双指针
def way2(nums):
    n = len(nums)
    p0 = p1 = 0
    for i in range(n):
        if nums[i] == 1:
            nums[i], nums[p1] = nums[p1], nums[i]
            p1 += 1
        elif nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            if p0 < p1:
                nums[i], nums[p1] = nums[p1], nums[i]
            p0 += 1
            p1 += 1
    return nums

#双指针2
def way3(nums):
    n = len(nums)
    p0, p2 = 0, n-1
    i = 0
    while i < p2:
        while i <= p2 and nums[i] == 2:
            nums[i], nums[p2] = nums[p2], nums[i]
            p2 -= 1
        if nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            p0 += 1
        i += 1
    return nums

# 三指针
def way4(nums):
    r, w, b = 0, 0, len(nums)-1
    while w < b:
        if nums[w] == 0:
            nums[w], nums[r] = nums[r], nums[w]
            r += 1
            w += 1
        elif nums[w] == 1:
            w += 1
        else:
            nums[w], nums[b] = nums[b], nums[w]
            b -= 1
    return nums


# 交换函数
def way5(nums):
    def swap(nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]
    size = len(nums)
    zero = 0
    two = size
    i = 0
    while i < two:
        if nums[i] == 0:
            swap(nums, i, zero)
            i += 1
            zero += 1
        elif nums[i] == 1:
            i += 1
        else:
            two -= 1
            swap(nums, i, two)






