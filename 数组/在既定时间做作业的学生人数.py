# 1450
# author jh
def busyStudent(startTime, endTime, queryTime):
    stu = 0
    for i in range(len(startTime)):
        if startTime[i] <= queryTime and endTime[i] >= queryTime:
            stu += 1
    return stu

#
def way2(startTime, endTime, queryTime):
    return sum([i <= queryTime <=j for i, j in zip(startTime, endTime)])

