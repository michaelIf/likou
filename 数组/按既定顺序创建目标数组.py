# 1389
# author jh
def createTargetArray(nums, index):
    res = []
    for i, j in zip(index, nums):
        res.insert(i, j)
    return res
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(createTargetArray(nums,index))

# author official
def way2(nums, index):
    res = []
    for i in range(len(nums)):
        res.insert(index[i], nums[i])
    return res