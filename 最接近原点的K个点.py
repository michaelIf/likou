# 暴力解法
def KClosest(points, k):
    if k <= 0:
        return None
    res = []
    for i in range(k):
        temp = points[0][0]**2 + points[0][1]**2
        tt = 0
        for j in range(len(points)):
            le = points[j][0]**2 + points[j][1]**2
            if le < temp:
                temp = le
                tt = j
        res.append(points[tt])
        points.pop(tt)
    return res

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
ss = KClosest(points, k)
print(ss)

# 排序
def KClosest2(points, K):
    points.sort(key=lambda x:(x[0]**2 + x[1]**2))
    return points[:K]

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
ss = KClosest2(points, k)
print(ss)

# 优先队列
# Python 语言中，优先队列为小根堆
def KClosest3(points, K):
    import heapq
    q = [(-x**2 - y**2, i) for i, (x, y) in enumerate(points[:K])]
    heapq.heapify(q)
    n = len(points)
    for i in range(K, n):
        x, y = points[i]
        dist = -x**2 - y**2
        heapq.heappushpop(q, (dist, i))
    ans = [points[identify] for (_, identify) in q]
    return ans







