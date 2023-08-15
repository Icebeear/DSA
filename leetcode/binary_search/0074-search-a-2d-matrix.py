class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid_row = (l + r) // 2 
            if matrix[mid_row][0] > target:
                r = mid_row - 1 
            elif matrix[mid_row][-1] < target: 
                l = mid_row + 1 
            else:
                break 

        matrix = matrix[mid_row]

        l, r = 0, len(matrix) - 1 

        while l <= r:
            mid = (l + r) // 2 
            if matrix[mid] == target:
                return True 
            elif matrix[mid] > target: 
                r = mid - 1 
            else:
                l = mid + 1 
        return False 
    
'''
https://leetcode.com/problems/search-a-2d-matrix/description/
-------------------------------------------------------------

'''