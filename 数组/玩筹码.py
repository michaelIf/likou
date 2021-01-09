# 1217
# 数学证明+贪心
# author 上杉绘梨衣
def minCostToMoveChips(position):
    odd = 0
    even = 0
    for i in position:
        if i % 2 == 0:
            odd += 1
        else:
            even += 1
    return min(odd, even)
