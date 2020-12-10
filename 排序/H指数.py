# 274
# 按数列逆序排序
# 取元素和下标值的最小值，并将结果放入一个列表
# 取出列表中的最大值
def hIndex(citations):
    if not citations:
        return 0
    citations.sort(reverse=True)
    le = len(citations)
    min_num = 0
    res = min(citations[0], 0)
    for i in range(le):
        min_num = min(citations[i], i+1)
        if min_num > res:
            res = min_num
    return res
# citations = [3,0,6,1,5]
# citations = [100]
# citations = [1, 2]
citations = [0,0]
print(hIndex(citations))
