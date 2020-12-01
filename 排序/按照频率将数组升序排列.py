#
def frequencySort(nums):
    temp_dict = {}
    res = []
    for i in nums:
        if i in temp_dict:
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1
    temp_dict = sorted(temp_dict.items(), key=lambda x: (x[1], -x[0]))
    res = []
    for key, value in temp_dict:
        res += [key] * value
    return res

nums = [2,3,1,3,2]
print(frequencySort(nums))



