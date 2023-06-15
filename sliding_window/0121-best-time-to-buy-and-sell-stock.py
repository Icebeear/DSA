class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0 
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price 
            profit = max(profit, price - lowest)
        return profit       
    
#O(n)
'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
--------------------------------------------------------------

'''
