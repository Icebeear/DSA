class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge_two_lists(a, b):
            res = []
            i, j = 0, 0 
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1 

            res += a[i:] + b[j:]
            return res

        def merge(arr):
            if len(arr) == 1:
                return arr 
            mid = len(arr) // 2 
            left = merge(arr[:mid])
            right = merge(arr[mid:])

            return merge_two_lists(left, right)

        return merge(nums)

'''
https://leetcode.com/problems/sort-an-array/description/
--------------------------------------------------------
сортировка слиянем
O(nlog(n))
'''