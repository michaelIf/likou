# 1486
# author jh
def xorOperation(n, start):
    res = start
    for i in range(1, n):
        res ^= (start + 2*i)
    return res
n = 5
start = 0
print(xorOperation(n, start))

