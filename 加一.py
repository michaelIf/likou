# 转换成数字加1
# 对于[0,0]这种情况无法通过


def plusOne(digits):
    str_d = ''
    for i in digits:
        str_d += str(i)
    int_d = int(str_d)
    int_d += 1
    res_s = str(int_d)
    res = []
    for i in str(res_s):
        res.append(int(i))
    return res


# 从后面判断是否为9
def way2(digits):
    res = []
    while digits and digits[-1] == 9:
        digits.pop()
        res.append(0)
    if not digits:
        return [1] + res
    else:
        digits[-1] += 1
        return digits + res












