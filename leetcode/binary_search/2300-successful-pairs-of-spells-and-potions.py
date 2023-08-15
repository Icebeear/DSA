class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        res = []
        potions.sort()
        for spell in spells: 
            l, r = 0, len(potions) - 1
            while l <= r:
                mid = (l + r) // 2 
                if potions[mid] * spell >= success:
                    r = mid - 1 
                else:
                    l = mid + 1
            res.append(len(potions) - l)
        return res 
    
'''
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
---------------------------------------------------------------------------------

'''