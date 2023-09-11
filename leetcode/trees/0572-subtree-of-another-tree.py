# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        if not root:
            return False 
        if root.val == subRoot.val:
            if self.isSame(root, subRoot):
                return True 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, r, s):
        if not r and not s:
            return True 
        if r and s and r.val == s.val:
            return self.isSame(r.left, s.left) and self.isSame(r.right, s.right)
        else:
            return False 

'''
https://leetcode.com/problems/subtree-of-another-tree/description/
------------------------------------------------------------------

'''