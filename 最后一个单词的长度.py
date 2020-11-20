# 暴力解法
def lengthOfLastWord(s):
    word_list = s.split()
    length = len(word_list)
    if length == 0:
        return 0
    elif length == 1:
        return len(word_list[0])
    else:
        return len(word_list[-1])
ss = "a"
tt = lengthOfLastWord(ss)
print(tt)



