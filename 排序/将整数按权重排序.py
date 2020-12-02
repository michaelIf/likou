# 权重升序，数值升序
def getKth(lo, hi, k):
    def get_qz(num):
        count = 0
        while num != 1:
            if num % 2 == 0:
                num /= 2
                count += 1
            else:
                num = 3 * num + 1
                count += 1
        return count
    temp_dict = {}
    for i in range(lo, hi + 1):
        qz = get_qz(i)
        temp_dict[i] = qz
    res_dict = sorted(temp_dict.items(), key=lambda x: (x[1], x[0]))
    res = res_dict[k-1][0]
    return res



print(getKth(12,15,2))






# def get_qz(num):
#     count = 0
#     while num != 1:
#         if num % 2 == 0:
#             num /= 2
#             count += 1
#         else:
#             num = 3 * num + 1
#             count += 1
#     return count