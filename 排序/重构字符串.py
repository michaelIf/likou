# 767
# 贪心+最大堆
def reorganizeString(S):
    le_s = len(S)
    if le_s < 2:
        return S
    temp_d = {}
    for i in S:
        if i in temp_d:
            temp_d[i] += 1
        else:
            temp_d[i] = 1

    if max(temp_d.values()) * 2 - 1 > le_s:
        return ''
    pq = []
    import heapq
    for key, val in temp_d.items():
        heapq.heappush(pq, (-val, key))
    prev = (0, None)
    res = ''
    while pq:
        v, k = heapq.heappop(pq)
        res += k
        if prev[0] < 0:
            heapq.heappush(pq, prev)
        prev = (v + 1, k)
    return res
S = "aab"
print(reorganizeString(S))
S = "aaab"
print(reorganizeString(S))
# from heapq import *
# from random import shuffle
# data = list(range(10))
# shuffle(data)
# heap = []
# for n in data:
#     heappush(heap, n)
# print(heap)
# heappush(heap, 0.5)
# print(heap)
# ss = heappop(heap)
# print(ss)
# print(heap)
# ss = heappop(heap)
# print(ss)
# print(heap)
# ss = heappop(heap)
# print(ss)
# print(heap)

