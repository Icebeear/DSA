class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            l = i + 1 
            r = len(nums) - 1 
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum > 0:
                    r -= 1 
                elif curSum < 0:
                    l += 1 
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1 
                    r -= 1 
        return ans 
#O(n^3)
'''
https://leetcode.com/problems/3sum/description/
-----------------------------------------------

'''