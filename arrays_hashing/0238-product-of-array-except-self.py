class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        step = 1 
        for i in range(len(nums)):
            res[i] = step
            step *= nums[i]

        step = 1 
        for i in range(len(nums) -1, -1, -1):
            res[i] *= step 
            step *= nums[i]

        return res

#O(n)
'''
https://leetcode.com/problems/product-of-array-except-self/description/
-----------------------------------------------------------------------
nums = [1, 2, 3, 4]
res = [1, 1, 1, 1]
Пробегаем по nums, слева на право, и меняем в res произведение всех слева и записываем это 
произведение в step 
--------
Потом справа на лево, но не меняем в res, a домножаем 
'''