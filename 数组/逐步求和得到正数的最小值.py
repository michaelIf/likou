# 1413
# author jh
# 取[:i]的最小值，如果都为正数，则结果为1
def minStartValue(nums):
    return (1 if min(sum(nums[:i+1]) for i in range(len(nums))) > 0 else 1 - min(sum(nums[:i+1]) for i in range(len(nums))))
# nums = [-3,2,-3,4,2]
nums = [1,2]
# nums = [1,-2,-3]
print(minStartValue(nums))



