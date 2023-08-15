class Solution:
    def findDuplicate(self, nums):
        hashset = {}
        for num in nums: 
            if num not in hashset: 
                hashset[num] = 1
            else: 
                hashset[num] += 1 
        return max(hashset.items(), key=lambda x: x[1])[0]
    
'''
https://leetcode.com/problems/find-the-duplicate-number/description/
--------------------------------------------------------------------
'''