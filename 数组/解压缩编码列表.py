# 1313
# for 循环
# author jh
def decompressRLElist(nums):
    res = []
    for i in range(0, len(nums), 2):
        res.extend([nums[i+1]]*nums[i])
    return res
nums = [1,2,3,4]
print(decompressRLElist(nums))


