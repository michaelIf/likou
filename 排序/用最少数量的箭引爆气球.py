# 452
# 排序+贪心算法
def findMinArrowShots(points):
    if not points:
        return 0
    points.sort(key=lambda bal: bal[1])
    pos = points[0][1]
    ans = 1
    for bal in points:
        if bal[0] > pos:
            pos = bal[1]
            ans += 1
    return ans








