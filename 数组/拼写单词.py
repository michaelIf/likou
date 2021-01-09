# 1160
# author jh
'''
先将chars 生成一个字典，然后遍历words，将在chars中的字符找到，
并将chars的值减一，如果此时chars的值小于0，则该单词不在chars中
为了每次遍历都可以操作chars，可以将字典深拷贝一份
'''

def countCharacters(words, chars):
    import copy
    letter_count = {}
    for i in chars:
        if i in letter_count:
            letter_count[i] += 1
        else:
            letter_count[i] = 1
    res = 0
    for j in words:
        temp = copy.deepcopy(letter_count)
        flag = 1
        for k in j:
            if k in temp:
                temp[k] -= 1
                if temp[k] < 0:
                    flag = 0
            else:
                flag = 0
        if flag == 1:
            res += len(j)
    return res
words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(countCharacters(words, chars))

# author official
# 直接比较两个字典的值，另类if else
def way2(words, chars):
    import collections
    chars_cnt = collections.Counter(chars)
    ans = 0
    for word in words:
        word_cnt = collections.Counter(word)
        for c in word_cnt:
            if chars_cnt[c] < word_cnt[c]:
                break
        else:
            ans += len(word)
    return ans




