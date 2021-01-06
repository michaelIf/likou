# 1266
# 切比雪夫距离
# official
def minTimeToVisitAllPoints(points):
    x0, x1 = points[0]
    ans = 0
    for i in range(1, len(points)):
        y0, y1 = points[i]
        ans += max(abs(x0-y0),abs(x1-y1))
        x0, x1 = points[i]
    return ans