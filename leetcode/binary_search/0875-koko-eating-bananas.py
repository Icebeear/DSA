from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        
        while l <= r:
            time = 0
            k = l + ((r - l) // 2)
            for pile in piles:
                time += ceil(pile / k)
            if time <= h:
                res = min(k, res)
                r = k - 1
            else:
                l = k + 1 
        return res 
#O(log(max(piles) * piles))

'''
https://leetcode.com/problems/koko-eating-bananas/description/
--------------------------------------------------------------

'''

