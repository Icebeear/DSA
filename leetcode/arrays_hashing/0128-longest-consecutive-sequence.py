class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        res = 0 
        for n in numset: 
            if n - 1 not in numset:
                lenght = 1 
                while (n + lenght) in numset:
                    lenght += 1 
                res = max(lenght, res)
        return res 

#O(n) 
'''
https://leetcode.com/problems/longest-consecutive-sequence/description/
-----------------------------------------------------------------------
последовательносто только если число больше на 1, и как только находим начало потенциальной последовательности,
идем вайлом пока не дойдем до края 
'''