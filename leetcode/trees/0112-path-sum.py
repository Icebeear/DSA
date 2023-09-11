# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False 

        stack = [(root, root.val)]

        while stack:
            cur, val = stack.pop()

            if not cur.left and not cur.right and val == targetSum:
                return True 

            if cur.left:
                stack.append((cur.left, cur.left.val + val))

            if cur.right:
                stack.append((cur.right, cur.right.val + val))

        return False 

'''
https://leetcode.com/problems/path-sum/description/
---------------------------------------------------

'''