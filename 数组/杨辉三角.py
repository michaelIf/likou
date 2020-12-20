# 118
# author jh
def generate(numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1],[1,1]]
    if numRows == 3:
        return [[1],[1,1],[1,2,1]]
    if numRows == 4:
        return [[1],[1,1],[1,2,1], [1,3,3,1]]
    if numRows == 5:
        return [[1],[1,1],[1,2,1], [1,3,3,1],[1,4,6,4,1]]
    if numRows ==6:
        return [[1],[1,1],[1,2,1], [1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]

# 使用一个临时列表
# author jh
def way2(numRows):
    res = []
    for i in range(numRows):
        temp = []
        if i == 0:
            temp =[1]
            res.append(temp)
        elif i == 1:
            temp = [1,1]
            res.append(temp)
        else:
            for j in range(len(res[-1])+1):
                if j == 0:
                    temp.append(res[-1][j])
                elif j <= len(res[-1])-1:
                    temp.append(res[-1][j-1]+res[-1][j])
                else:
                    temp.append(res[-1][-1])
            res.append(temp)
    return res
print(way2(5))




