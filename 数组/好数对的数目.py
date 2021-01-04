# 1512
# 双for循环
# author jh
def numIdenticalPairs(nums):
    le = len(nums)
    res = 0
    for i in range(le):
        for j in range(i+1, le):
            if nums[i] == nums[j]:
                res += 1
    return res

nums = [1,2,3,1,1,3]
# print(numIdenticalPairs(nums))

# 先生成字典
# author jh
def way2(nums):
    import collections
    d = collections.Counter(nums)
    res = 0
    for k, v in d.items():
        if v >= 2:
            res += (v-1)*v//2
    return res
print(way2(nums))



