# 1629
# author jh
def slowestKey(releaseTimes, keysPressed):
    d = {}
    d[keysPressed[0]] = releaseTimes[0]

    for i in range(1, len(keysPressed)):
        if keysPressed[i] not in d:
            d[keysPressed[i]] = releaseTimes[i] - releaseTimes[i - 1]
        else:
            if d[keysPressed[i]] < releaseTimes[i] - releaseTimes[i - 1]:
                d[keysPressed[i]] = releaseTimes[i] - releaseTimes[i - 1]
    res = sorted(d.items(), key=lambda x: (x[1], x[0]))
    return res[-1][0]

releaseTimes = [9,29,49,50]
keysPressed = "cbcd"
print(slowestKey(releaseTimes,keysPressed))

# 贪心算法
# author JHMDL
def way2(releaseTimes, keysPressed):
    n = len(releaseTimes)
    last = longest = releaseTimes[0]
    ans = keysPressed[0]
    for i in range(1, n):
        last_time = releaseTimes[i] - last
        if last_time > longest:
            longest = last_time
            ans = keysPressed[i]
        elif last_time == longest:
            ans = max(ans, keysPressed[i])
        last = releaseTimes[i]
    return ans







