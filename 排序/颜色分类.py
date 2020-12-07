# 75
# sort
def sortColors(nums):
    return nums.sort()



# 冒泡排序
def way2(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            temp = 0
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums


nums = [2,0,2,1,1,0]
print(way2(nums))

# 快速排序
def way3(nums):
        def swap(nums, index1, index2):
            nums[index1],nums[index2] = nums[index2], nums[index1]
        size = len(nums)
        if size < 2:
            return
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
        return nums

# 三指针
'''
两个指针记录0和2的边界；
第三个指针遍历；
遇到0就跟第一个指针交换；
遇到2就跟第二个指针交换；
'''
def way4(nums):
    p0, cur, p2 = 0, 0, len(nums) - 1
    while cur < p2:
        if nums[cur] == 0:
            nums[p0], nums[cur] = nums[cur], nums[p0]
            p0 += 1
            cur += 1
        elif nums[cur] == 2:
            nums[cur], nums[p2] = nums[p2], nums[cur]
            p2 -= 1
        else:
            cur += 1
    return nums
