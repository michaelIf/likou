# 853
# 排序+单调栈
def carFleet(target, position, speed):
    cars = sorted(zip(position, speed))
    times = [float(target - p) / s for p, s in cars]
    ans = 0
    while len(times) > 1:
        lead = times.pop()
        if lead < times[-1]:
            ans += 1
        else:
            times[-1] = lead
    return ans + bool(times)
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target, position, speed))
