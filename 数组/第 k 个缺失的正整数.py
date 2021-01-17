# 1539
# author official
# 枚举
def findKthPositive(arr, k):
    missCount = 0
    lastMiss = -1
    current = 1
    ptr = 0
    while missCount < k:
        if current == arr[ptr]:
            if ptr + 1 < len(arr):
                ptr += 1
        else:
            missCount += 1
            lastMiss = current
        current += 1
    return lastMiss



