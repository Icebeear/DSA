class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        res = 0 
        stack = [] # pair: [index, height]
        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                area = (i - stack[-1][0]) * stack[-1][1]
                res = max(res, area)
                start = stack[-1][0]
                stack.pop()
            stack.append([start, h])

        for i, h in stack:
            res = max(res, h * (len(heights) - i))

        return res 

#O(n)    
'''
https://leetcode.com/problems/largest-rectangle-in-histogram/description/
-------------------------------------------------------------------------


'''