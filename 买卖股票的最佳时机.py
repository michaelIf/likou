# 动态规划
def maxProfit(prices):
    le = len(prices)
    dp = [[0, 0] for _ in range(le)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, le):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 0][0] - prices[i])
    return dp[le - 1][0]


tt = [7,1,5,3,6,4]
ss = maxProfit(tt)
print(ss)


# 动态规划优化
def maxProfit2(prices):
    size = len(prices)
    dp0 = 0
    dp1 = -prices[0]
    for i in range(1, size):
        tmp = dp0
        dp0 = max(dp0, dp1 + prices[i])
        dp1 = max(dp1, tmp - prices[i])
    return dp0


# 贪心算法
def maxProfit3(prices):
    size = len(prices)
    ans = 0
    for i in range(1, size):
        ans += max(0, prices[i] - prices[i - 1])
    return ans
tt = [7,1,5,3,6,4]
ss = maxProfit3(tt)
print(ss)








    

