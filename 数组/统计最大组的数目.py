# 1399
# 字典
# author official
def countLargestGroup(n):
    import collections
    d = collections.Counter()
    for i in range(1, n+1):
        key = sum([int(x) for x in str(i)])
        d[key] += 1
    maxValue = max(d.values())
    count = sum(1 for v in d.values() if v == maxValue)
    return count

