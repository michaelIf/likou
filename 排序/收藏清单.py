#
def peopleIndexes(favoriteCompanies):
    le_fa = len(favoriteCompanies)
    res = []
    for i in range(le_fa):
        le_i = len(favoriteCompanies[i])
        count = 0
        k = 0
        for j in range(le_i):
            if k != i and favoriteCompanies[i][j] in favoriteCompanies[k]:
                count += 1
            else:
                k += 1
                break
        if count == le_i:
            res.append(i)
            break
    tmp_list = []
    for i in range(le_fa):
        tmp_list.append(i)
    for j in res:
        tmp_list.remove(j)
    return tmp_list

favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
print(peopleIndexes(favoriteCompanies))


# 使用set
# 判断两集合的交集是否为某一集合 x&y == x ，来确定清单
def way2(favoriteCompanies):
    ans = []
    favoriteCompanies = [set(x) for x in favoriteCompanies]
    for i, x in enumerate(favoriteCompanies):
        flag = 0
        for j, y in enumerate(favoriteCompanies):

            if i == j:
                continue
            if x & y == x:
                flag = 1
                break
        if flag == 0:
            ans.append(i)
    return ans
favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
print(way2(favoriteCompanies))


