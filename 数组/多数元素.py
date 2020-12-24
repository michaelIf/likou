# 169
# author jh
def majorityElement(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    temp = 0
    res = 0
    for j, k in d.items():
        if k > temp:
            temp = k
            res = j
    return res

nums = [2,2,1,1,1,2,2]
# print(majorityElement(nums))

# 使用counter和sorted
# author jh
def way2(nums):
    import collections
    dd = collections.Counter(nums)
    ss = sorted(dd.items(), key=lambda x: (x[1]))
    return ss[-1][0]

# print(way2(nums))

# 投票算法
# author official
def way3(nums):
    count = 0
    can = None
    for num in nums:
        if count == 0:
            can = num
        count += (1 if num == can else -1)
    return can

print(way3(nums))


