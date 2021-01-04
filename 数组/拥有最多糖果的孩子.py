# 1431
# author jh
def kidsWithCandies(candies, extraCandies):
    res = []
    for i in candies:
        if i + extraCandies >= max(candies):
            res.append(True)
        else:
            res.append(False)
    return res

candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies,extraCandies))

# author 时、倾
def way2(candies, extraCandies):
    max_c = max(candies)
    res = []
    for i in candies:
        res.append(i+ extraCandies>= max_c)
    return res







