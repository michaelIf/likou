# 948
# 队列 + 贪心
# author 官方
def bagOfTokensScore(tokens, P):
    import collections
    tokens.sort()
    deque = collections.deque(tokens)
    ans = bns = 0
    while deque and (P >= deque[0] or bns):
        while deque and P >= deque[0]:
            P -= deque.popleft()
            bns += 1
        ans = max(ans, bns)
        if deque and bns:
            P += deque.pop()
            bns -= 1
    return ans

# 双指针 + 贪心
# author hahahu
def way2(tokens, P):
    tokens.sort()
    b = 0
    t = len(tokens) - 1
    cur = 0
    ret = 0
    while b <= t:
        while b <= t and P > tokens[b]:
            P -= tokens[b]
            b += 1
            cur += 1
            ret = max(ret, cur)
        if cur <= 0:
            break
        if b <= t:
            cur -= 1
            P += tokens[t]
            t -= 1
    return ret







