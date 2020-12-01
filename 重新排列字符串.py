# 自己动手
def restoreString(s, indices):
    res = [ 0 for i in range(len(s))]
    res_s = ''
    for i, j in zip(indices, s):
        res[i] = j
    for j in res:
        res_s += j

    return res_s


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s,indices))


# 一次遍历
def way2(s, indices):
    res = ["" for i in range(len(s))]
    for i in range(len(s)):
        res[indices[i]] = s[i]
    return "".join(res)