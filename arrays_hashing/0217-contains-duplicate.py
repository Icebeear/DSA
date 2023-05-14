class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums: 
            if n in hashset: 
                return True 
            hashset.add(n)
        return False 
    
'''
https://leetcode.com/problems/contains-duplicate/
-------------------------------------------------
Итерируемся по nums, если n в хешсете, а он содержит только уникальные -> то ретернем true 
если пройдемся по nums и все уникальное то false 
'''