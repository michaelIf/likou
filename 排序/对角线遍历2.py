
# nums[i][j] 必然在第（i + j）次斜线的结果中。i 越小，结果越靠后。
def way2(nums):
    sub_res = []
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if i + j >= len(sub_res):
                sub_res.append([])
            sub_res[i + j].append(nums[i][j])
    res = []
    for sub in sub_res:
        res += sub[::-1]
    return res

nums = [[1,2,3],[4,5,6],[7,8,9]]
print(way2(nums))

# 使用字典
def way3(nums):
    from collections import defaultdict
    tmp = defaultdict(list)
    for row in range(len(nums)):
        for col in range(len(nums[row])):
            tmp[row + col].append(nums[row][col])
    res = []
    for r_plus_c in sorted(list(tmp.keys())):
        res.extend(tmp[r_plus_c][::-1])
    return res

nums = [[1,2,3],[4,5,6],[7,8,9]]
print(way3(nums))
