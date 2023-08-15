class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:    
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)
        
        return [left, right]

    #route = (True / False), True if we moving left, if right then False 
    def binary_search(self, nums, target, route):
        l, r = 0, len(nums) - 1 
        i = -1 
        while l <= r:
            mid = (l + r) // 2 
            if nums[mid] > target: 
                r = mid - 1 
            elif nums[mid] < target:
                l = mid + 1 
            else:
                i = mid 
                if route:
                    r = mid - 1 
                else:
                    l = mid + 1 
        return i 
    
'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
--------------------------------------------------------------------------------------------------

'''