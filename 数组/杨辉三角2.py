# 119
# 和杨辉三角1中方法一致
# author jh
def getRow(rowIndex):
    res = []
    for i in range(rowIndex+1):
        temp = []
        if i == 0:
            temp = [1]
            res.append(temp)
        elif i == 1:
            temp = [1, 1]
            res.append(temp)
        else:
            for j in range(len(res[-1]) + 1):
                if j == 0:
                    temp.append(res[-1][j])
                elif j <= len(res[-1]) - 1:
                    temp.append(res[-1][j - 1] + res[-1][j])
                else:
                    temp.append(res[-1][-1])
            res.append(temp)
    return res[-1]

# author leichaojian
# j行的数据, 应该由j - 1行的数据计算出来.
# 假设j - 1行为[1,3,3,1], 那么我们前面插入一个0(j行的数据会比j-1行多一个),
# 然后执行相加[0+1,1+3,3+3,3+1,1] = [1,4,6,4,1], 最后一个1保留即可.
def way2(rowIndex):
    r = [1]
    for i in range(1, rowIndex+1):
        r.insert(0, 0)
        for j in range(i):
            r[j] = r[j] + r[j+1]
    return r

print(way2(2))









