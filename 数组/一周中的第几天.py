# 1185
# 使用现有库
def dayOfTheWeek(day, month, year):
    import datetime
    week_day_dict = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
    }
    anyday = datetime.datetime(year, month, day).strftime('%w')
    return week_day_dict[int(anyday)]
print(dayOfTheWeek(31,8,2019))

#
# 手动计算
def way2(day, month, year):
    # 1971年1月1日为星期五
    res = ["Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    days = -1
    for y in range(1971, year):
        if isLeapYear(y):
            days += 366
        else:
            days += 365
    for m in range(1, month):
        if m == 2:
            if isLeapYear(year):
                days += 29
            else:
                days += 28
        elif m in [1,3,5,7,8,10,12]:
            days += 31
        else:
            days += 30
    days += day
    return res[days%7]
def isLeapYear(year):
    if year % 400 == 0: return True
    if year % 4 == 0 and year % 100 != 0: return True
    return False

print(way2(31,8,2019))