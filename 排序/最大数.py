# 179
# 比较运算符重载后排序
'''
重载比较运算符 lt(less than)
将数组中所有元素类型改为字符串
对数组排序，key 为重载后的 lt
将排序后的数组拼接起来输出
如果第一个元素就为 ‘0’，说明所有元素均为 ‘0’，则返回 ‘0’
'''

class StrLt(str):
    def __lt__(x, y):
        return x + y > y + x

def largestNumber(nums):
    strn = [str(n) for n in nums]
    strn.sort(key=StrLt)
    return ''.join(strn) if strn[0] != '0' else '0'
# nums = [10,2]
nums = [3,30,34,5,9]
print(largestNumber(nums))

# 字符串转化为浮点数排序
def way2(nums):
    def bi(i):
        if i == 0:
            return 0
        s = 0
        k = i
        while i >= 1:
            i = i / 10
            s += 1
        return k / (10 ** s - 1)

    nums = sorted(nums, key=bi, reverse=True)
    if nums[0] == 0:
        return "0"
    return "".join([str(i) for i in nums])

nums = [3,30,34,5,9]
print(way2(nums))
