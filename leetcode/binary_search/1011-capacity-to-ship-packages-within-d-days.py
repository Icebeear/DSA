class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            mid_capacity = (l + r) // 2
            ship_days = 1 
            cur_weight = 0 
            for weight in weights:
                if (mid_capacity - cur_weight) >= weight:
                    cur_weight += weight
                else:
                    cur_weight = weight
                    ship_days += 1 

            if ship_days > days:
                l = mid_capacity + 1 
            else:
                r = mid_capacity
        return l
    
'''
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
----------------------------------------------------------------------------------

'''