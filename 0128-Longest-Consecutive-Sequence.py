class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        longest = 0 

        for num in numset:
            if num - 1 not in numset:
                lenght = 1  
                while (num + lenght) in numset:
                    lenght += 1 
                longest = max(lenght, longest)
        return longest 
    
'''
https://leetcode.com/problems/longest-consecutive-sequence/description/
-----------------------------------------------------------------------

'''