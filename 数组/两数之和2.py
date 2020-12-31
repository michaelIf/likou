# 167
# 双指针
# author jh
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    # le = len(numbers)
    while right > left:
        if numbers[right] + numbers[left] > target:
            right -= 1
        elif numbers[right] + numbers[left] < target:
            left += 1
        else:
            return [left+1, right+1]
    return False
numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))

# 二分查找
# author official
def way2(numbers, target):
    n = len(numbers)
    for i in range(n):
        low, high = i + 1, n - 1
        while low < high:
            mid = (low + high) // 2
            if numbers[mid] == target - numbers[i]:
                return [i + 1, mid + 1]
            elif numbers[mid] > target - numbers[i]:
                high = mid - 1
            else:
                low = mid + 1
    return False