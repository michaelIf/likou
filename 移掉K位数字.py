# 暴力解法
def removeKdigits(num, k):
    def remove_0(ss):
        if ss[0] == "0":
            return remove_0(ss[1:])
        else:
            return ss
    length_num = len(num)
    if length_num == 0:
        return 0
    if length_num == k:
        return '0'

    min_num = int(num[0])
    min_num_i = 0
    for i in range(length_num):
        min_num = min(min_num, int(num[i]))
    for j in range(length_num):
        if min_num == int(num[j]):
            min_num_i = j
            break
    if k == min_num_i:
        res = num[k:]
        res = remove_0(res)
        return res

    def delete_max(ss, index):

        new_ss = ss[:index] + ss[index+1:]
        return new_ss

    def find_max(ss):
        max_temp = int(ss[0])
        max_temp_i = 0
        le = len(ss)
        for p in range(le):
            max_temp = max(max_temp, int(ss[p]))
        for q in range(le):
            if max_temp == int(ss[q]):
                max_temp_i = q
                break
        return max_temp_i




    if k < min_num_i:
        head = num[:min_num_i]
        for i in range(k):
            index_max = find_max(head)
            head = delete_max(head, index_max)
        res = head + num[min_num_i:]
        res = remove_0(res)
        return res
    if k > min_num_i:
        tail = num[min_num_i:]
        for j in range(k - min_num_i):
            index_max = find_max(tail)
            tail = delete_max(tail, index_max)
        return tail


num = "10200"
k = 1
ss = removeKdigits(num, k)
print(ss)

# num = "4322119"
# k = 2
# tt = removeKdigits(num, k)
# print(tt)

# def find_max(ss):
#     max_temp = int(ss[0])
#     max_temp_i = 0
#     le = len(ss)
#     for p in range(le):
#         max_temp = max(max_temp, int(ss[p]))
#     for q in range(le):
#         if max_temp == ss[q]:
#             max_temp_i = q
#             break
#     return max_temp_i
#
# tt = find_max('124248')
# print(tt)

# def remove_0(ss):
#     if ss[0] == "0":
#         return remove_0(ss[1:])
#     else:
#         return ss
#
#
# yy = '00000000000000000212312'
# tt = remove_0(yy)
# print(tt)

# 贪心算法 + 单调栈


def way2(num, k):
    numStack = []
    for digit in num:
        while k and numStack and numStack[-1] > digit:
            numStack.pop()
            k -= 1
        numStack.append(digit)
    finalStack = numStack[:-k] if k else numStack
    return "".join(finalStack).lstrip('0') or "0"







