# 350
# 一步一步走
'''
第一步将数组生成字典,统计每个元素的次数
第二步将在两个字典都存在的元素取出来
第三步将在两个字典中计数次数较少的取出来
第四步将较少的次数和元素生成结果列表
'''
def intersect(nums1, nums2):
    d1 = {}
    d2 = {}
    for i in nums1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for j in nums2:
        if j in d2:
            d2[j] += 1
        else:
            d2[j] = 1
    temp = []
    for m in d1.keys():
        if m in d2.keys():
            temp.append(m)
    res = []
    for n in temp:
        min_times = min(d1[n], d2[2])
        for k in range(min_times):
            res.append(n)
    return res

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersect(nums1,nums2))

# 双指针
def way2(nums1, nums2):
    nums1.sort()
    nums2.sort()
    res = []
    left, right = 0, 0
    while left < len(nums1) and right < len(nums2):
        if nums1[left] < nums2[right]:
            left += 1
        elif nums1[left] == nums2[right]:
            res.append(nums1[left])
            left += 1
            right += 1
        else:
            right += 1
    return res

