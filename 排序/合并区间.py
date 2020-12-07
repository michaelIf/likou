# 56
'''
先按首位置进行排序;
接下来,如何判断两个区间是否重叠呢?比如 a = [1,4],b = [2,3]
当 a[1] >= b[0] 说明两个区间有重叠.
但是如何把这个区间找出来呢?
左边位置一定是确定，就是 a[0]，而右边位置是 max(a[1], b[1])
所以,我们就能找出整个区间为:[1,4]
'''
def merge(intervals):
    if not intervals:
        return []
    intervals.sort()
    res = [intervals[0]]
    for x, y in intervals[1:]:
        if res[-1][1] < x:
            res.append([x, y])
        else:
            res[-1][1] = max(y, res[-1][1])
    return res




intervals = [[1, 3], [2, 6], [8, 10], [15, 18],[2,4],[5,6],[14,18]]
out = [[1,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# out = [[1,5]]

print(merge(intervals))