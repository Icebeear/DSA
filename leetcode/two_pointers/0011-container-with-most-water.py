class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1 
        while l < r: 
            area = min(height[l], height[r]) * (r - l)
            ans = max(area, ans)
            if height[l] < height[r]:
                l += 1 
            else:
                r -= 1 
        return ans 

#O(n)
'''
https://leetcode.com/problems/container-with-most-water/description/
--------------------------------------------------------------------
Двигаем тот указатель, у которого меньше стена 
'''