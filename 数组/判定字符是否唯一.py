# 面试题01.01
# author jh
# 双for循环
def isUnique(astr):
    for i in range(len(astr)):
        for j in range(i + 1, len(astr)):
            if astr[i] == astr[j]:
                return False
    return True

s = "leetcode"
# s = "abc"
# print(isUnique(s))


# 一次遍历
# author jh
def way2(astr):
    for i in range(len(astr)):
        if astr[i] in astr[i+1:]:
            return False
    return True
print(way2(s))

# 位运算
'''
我们可以使用一个int类型的变量（下文用mark表示）来代替长度为26的bool数组。
假设这个变量占26个bit（在多数语言中，这个值一般不止26），那么我们可以把它看成000...00(26个0)，
这26个bit对应着26个字符，对于一个字符c，检查对应下标的bit值即可判断是否重复。那么难点在于如何检查？
这里我们可以通过位运算来完成。首先计算出字符char离'a'这个字符的距离，即我们要位移的距离，用move_bit表示，
那么使用左移运算符1 << move_bit则可以得到对应下标为1，其余下标为0的数，如字符char = 'c'，
则得到的数为000...00100，将这个数跟mark做与运算，由于这个数只有一个位为1，其他位为0，
那么与运算的结果中，其他位肯定是0，而对应的下标位是否0则取决于之前这个字符有没有出现过，
若出现过则被标记为1，那么与运算的结果就不为0；若之前没有出现过，则对应位的与运算的结果也是0，
那么整个结果也为0。对于没有出现过的字符，我们用或运算mark | (1 << move_bit)将对应下标位的值置为1。
'''
# author 珍珠好好吃
def way3(astr):
    mark = 0
    for char in astr:
        move_bit = ord(char) - ord('a')
        if (mark & (1 << move_bit)) != 0:
            return False
        else:
            mark |= (1 << move_bit)
    return True

