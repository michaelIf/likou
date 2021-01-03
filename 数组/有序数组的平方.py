# 977
# author jh
def sortedSquares(nums):
    res = []
    for i in nums:
        temp = i * i
        res.append(temp)
    res.sort()
    return res

# official
def way2(nums):
    return sorted(num * num for num in nums)

# 双指针
def way3(nums):
    n = len(nums)
    negative = -1
    for i, num in enumerate(nums):
        if num < 0:
            negative = i
        else:
            break
    ans = list()
    i, j = negative, negative + 1
    while i >= 0 or j < n:
        if i < 0:
            ans.append(nums[j]*nums[j])
            j += 1
        elif j == n:
            ans.append(nums[i]*nums[i])
            i -= 1
        elif nums[i]*nums[i] < nums[j]*nums[j]:
            ans.append(nums[i]*nums[i])
            i -= 1
        else:
            ans.append(nums[j] * nums[j])
            j += 1
    return ans

# 双指针2
def way4(nums):
    n = len(nums)
    ans = [0] * n
    i, j, pos = 0, n-1, n-1
    while i <= j:
        if nums[i]*nums[i] > nums[j]*nums[j]:
            ans[pos] = nums[i]*nums[i]
            i += 1
        else:
            ans[pos] = nums[j]*nums[j]
            j -= 1
        pos -= 1
    return ans


    

