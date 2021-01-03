# 1331
'''
先用集合去重，再转为list，然后调用排序函数
最后用hashmap映射出转化后的序号
'''
# author 诺克萨斯之手
def arrayRankTransform(arr):
    hashmap = {}
    L = sorted(list(set(arr)))
    for i, num in enumerate(L):
        hashmap[num] = i + 1
    return [hashmap[i] for i in arr]

# arr = [40,10,20,30]
# arr = [100,100,100]
arr = [37,12,28,9,100,56,80,5,12]
print(arrayRankTransform(arr))





