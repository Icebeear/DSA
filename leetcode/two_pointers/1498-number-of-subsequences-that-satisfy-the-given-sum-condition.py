class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()

        l, r = 0, len(nums) - 1 
        res = 0 

        while l <= r:
            if nums[l] + nums[r] <= target:
                res += 1 << (r - l)
                l += 1 
            else:
                r -= 1 

        return res % (10**9 + 7)

'''
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/
------------------------------------------------------------------------------------------------------
сразу чекаем самое большое и самое маленькое, если подходят,
то добавляем в res += 2 ** (r - l) ( то есть количество подпоследовательностей)
'''