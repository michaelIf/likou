# 1295
# 将数字转化为字符串
# author jh
def findNumbers(nums):
    res = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            res += 1
    return res

# 取余
# author jh
def way2(nums):
    res = 0
    for i in nums:
        if i % 10 == i:
            pass
        elif i % 100 == i:
            res += 1
        elif i % 1000 == i:
            pass
        elif i % 10000 == i:
            res += 1
        elif i % 100000 == i:
            pass
        else:
            res += 1
    return res

nums = [100000]
print(way2(nums))
