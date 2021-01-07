# 1002
# author official
# 使用一个长度为26的列表保存每个字符的次数
def commonChars(A):
    minfreq = [float("inf")] * 26
    for word in A:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        for i in range(26):
            minfreq[i] = min(minfreq[i], freq[i])
    ans = []
    for i in range(26):
        ans.extend([chr(i + ord("a"))] * minfreq[i])
    return ans

# author zyyyyy
def way2(A):
    from collections import Counter
    res = None
    for a in A:
        c = Counter(a)
        if res is None:
            res = c
        else:
            res &= c
    return list(res.elements())

# 一行
def way3(A):
    import collections
    from functools import reduce
    return list(reduce(lambda x, y: x & y, map(collections.Counter, A)).elements())



    







A = ["bella","label","roller"]
print(commonChars(A))