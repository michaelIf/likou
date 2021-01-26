# 美团面试题
'''
分解质因数
'''
def feijie(n):
    def jundge(m):
        for i in range(2, m):
            if m % i == 0:
                return False
        return True
    s = 2
    res = []
    while 1:
        if jundge(n):
            res.append(n)
            break
        else:
            for i in range(2, n//2 + 1):
                if n % i == 0:
                    if jundge(i):
                        res.append(i)
                        n = n // i


    return res

print(feijie(124))




