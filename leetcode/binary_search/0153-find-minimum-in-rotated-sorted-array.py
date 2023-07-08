class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1 
        res = 5000
        while l <= r:
            mid = l + ((r - l) // 2)
            res = min(res, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1 
            else:
                r = mid - 1 
        return min(res, nums[l])
    
#O(logn)

'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
-------------------------------------------------------------------------------
Если nums[r] больше nums[mid], то мы идем вправо к нему иначе влево. В финале у нас остается nums из двух чисел
и мы берем min из  res и nums[l]
'''