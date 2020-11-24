# 暴力解法
def minWindow(s, t):
    index_dict = {}
    for i in t:
        temp_list = []
        for j in range(len(s)):
            if i == s[j]:
                temp_list.append(j)
        if not temp_list:
            return ''
        index_dict[i] = temp_list
    for m, n in index_dict.items():
        for p in n:
            pass


# 滑动窗口
def way2(s, t):
    import collections
    need = collections.defaultdict(int)
    for c in t:
        need[c] += 1
    needcnt = len(t)
    i = 0
    res = (0, float('inf'))
    for j, c in enumerate(s):
        if need[c] > 0:
            needcnt -= 1
        need[c] -= 1
        if needcnt == 0:
            while True:
                c = s[i]
                if need[c] == 0:
                    break
                need[c] += 1
                i += 1
            if j - i < res[1] - res[0]:
                res = (i, j)
            need[s[i]] += 1
            needcnt += 1
            i += 1
    return '' if res[1] > len(s) else s[res[0]: res[1] + 1]









