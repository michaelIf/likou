# 暴力解法
class Solution:
    def maxArea(self, height: list):
        le = len(height)
        res = 0
        for i in range(le):
            ss = 0
            for j in range(i+1, le):
                if height[i] > height[j]:
                    ss = height[j] * (j - i)
                else:
                    ss = height[i] * (j - i)
                if ss > res:
                    res = ss


        return res


pp = [1, 3, 4]
tt = Solution()
kk = tt.maxArea(pp)
print(kk)
# 双指针
class Soul:
    def maxArea(self, height):
        l, r = 0, len(height)-1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans









