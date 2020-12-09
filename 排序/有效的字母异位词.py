# 242
# 用两个字典比较
def isAnagram(s, t):
    d1 = {}
    d2 = {}
    for i in s:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for j in t:
        if j in d2:
            d2[j] += 1
        else:
            d2[j] = 1
    return d1 == d2

# 内置函数
def way2(s, t):
    import collections
    return collections.Counter(s) == collections.Counter(t)
