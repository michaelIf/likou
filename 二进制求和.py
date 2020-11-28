# python 内置函数
def addBinary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


# 2进制加法
def way2(a, b):
    r, p = '', 0
    d = len(b) - len(a)
    a = '0' * d + a
    b = '0' * -d + b
    print('a is %s' % a)
    print('b is %s' % b)
    for i, j in zip(a[::-1], b[::-1]):
        s = int(i) + int(j) + p
        r = str(s % 2) + r
        p = s // 2
        print('s is %d' % s)
        print('r is %s' % r)
        print('p is %d' % p)
    return '1' + r if p else r


a = '11'
b = '1'
print(way2(a, b))
