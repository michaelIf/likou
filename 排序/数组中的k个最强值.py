# sorted 配合lambda
def getStrongest(arr, k):
    arr.sort()
    res = {}
    m_index = (len(arr)-1)/2
    m = arr[int(m_index)]
    for j, x in enumerate(arr):
        res[j] = abs(m-x)
    res_dict = sorted(res.items(), key=lambda y: (-y[1], -y[0]))
    ans = []
    for n in range(k):
        ans.append(arr[res_dict[n][0]])
    return ans

# arr = [1,2,3,4,5]
# k = 2
arr = [-7,22,17,3]
k = 2
print(getStrongest(arr,k))

# 简洁版，不需要借助字典
def way2(arr,k):
    n = len(arr)
    arr = sorted(arr)
    mid = arr[(n-1)//2]
    def mykey(x):
        return (abs(x-mid),x)
    arr = sorted(arr,key=mykey)
    return arr[n-k:]

arr = [-7,22,17,3]
k = 2
print(way2(arr,k))



