# while
def canFormArray(arr, pieces):
    i = 0
    while (i < len(arr)):
        T = 0
        for j in range(i + 1, len(arr) + 1):
            if arr[i:j] in pieces:
                T = 1
                break
        if T == 0:
            return False
        else:
            i = j
    return True

# arr = [49,18,16]
# pieces = [[16,18,49]]
# print(canFormArray(arr,pieces))

def way2(arr, pieces):
    price_dic = {}
    for i, price in enumerate(pieces):
        price_dic[price[0]] = i
    narr = len(arr)
    res = []
    print(price_dic)
    for i in range(narr):
        if arr[i] in price_dic:
            res += pieces[price_dic[arr[i]]]
    return res == arr
arr = [49,18,16]
pieces = [[49,18],[16]]
print(way2(arr,pieces))



