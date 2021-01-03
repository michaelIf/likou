# 1480
# author jh
def runningSum(nums):
    res = []
    temp = 0
    for i in range(len(nums)):
        temp += nums[i]
        res.append(temp)
    return res
nums = [1,2,3,4]
print(runningSum(nums))

# 剩空间的做法
# author 痞痞的嘉诚
'''
思路非常简单，我们可以利用原来的数组，这样空间内存就省下来了
从第二个元素开始遍历数组，当前位置等于当前位置的值加上上一个位置的值
最后返回数组
'''
def way2(nums):
    if not nums:
        return []
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
    return nums



