# 作业帮面试题
#

def find_prime(nums):
    result = []
    for num in nums:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                result.append(num)
        else:
            pass
    return result

print(find_prime([2,3,5,11,12]))
