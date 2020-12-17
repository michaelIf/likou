# 969
# 思路/先找到最大值的index，然后将其翻转到第一位，然后在翻转到最后一位
# author Hao Guo
def pancakeSort(A):
    i, res = len(A), []
    while i > 0:
        max_idx = A[:i].index(i)
        if max_idx != i - 1:
            A[:max_idx+1] = A[:max_idx+1][::-1]
            A[:i] = A[:i][::-1]
            res.extend([max_idx+1, i])
        i -= 1
    return res

A = [3,2,4,1]
print(pancakeSort(A))


'''
思路
我们可以将最大的元素（在位置 i，下标从 1 开始）进行煎饼翻转 i 操作将它移动到序列的最前面，然后再使用煎饼翻转 A.length 操作将它移动到序列的最后面。 此时，最大的元素已经移动到正确的位置上了，所以之后我们就不需要再使用 k 值大于等于 A.length 的煎饼翻转操作了。
我们可以重复这个过程直到序列被排好序为止。 每一步，我们只需要花费两次煎饼翻转操作。
算法
我们从数组 A 中的最大值向最小值依次进行枚举，每一次将枚举的元素放到正确的位置上。
每一步，对于在位置 i 的（从大到小枚举的）元素，我们会使用思路中提到的煎饼翻转组合操作将它移动到正确的位置上。 值得注意的是，执行一次煎饼翻转操作 f，会将位置在 i, i <= f 的元素翻转到位置 f+1 - i 上。
'''
# author 官方
def way2(A):
    ans = []
    N = len(A)
    B = sorted(range(1, N+1), key=lambda i: -A[i-1])
    for i in B:
        for f in ans:
            if i <= f:
                i = f+1-i
        ans.extend([i, N])
        N -= 1
    return ans

