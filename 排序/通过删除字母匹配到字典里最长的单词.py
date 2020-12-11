# 524
# 排序+双指针
def findLongestWord(s,d):
    ans, ans_len = '', 0
    for dstr in d:
        i = j = 0
        while i < len(s) and j < len(dstr):
            if s[i] == dstr[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == len(dstr):
            if j > ans_len:
                ans, ans_len = dstr, j
            elif j == ans_len and dstr < ans:
                ans, ans_len = dstr, j
    return ans

# sort + find
def way2(s, d):
    d.sort(key=lambda x: (-len(x), x))
    for word in d:
        index = 0
        for ch in word:
            index = s.find(ch, index) + 1
            if not index:
                break
        else:
            return word
    return ''

s = "abpcplea"
d = ["ale","apple","monkey","plea"]
print(way2(s,d))
print(findLongestWord(s,d))




