# 1672
# author jh
def maximumWealth(accounts):
    ans = sum(accounts[0])
    for i in accounts:
        temp = sum(i)
        if temp > ans:
            ans = temp
    return ans

# author jh
def way2(accounts):
    return max(sum(i) for i in accounts)


