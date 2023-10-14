# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        if not root or (not root.left and not root.right):
            return True

        if root.left and root.right:
            def dfs(l, r):
                if not l and not r:
                    return True 
                if l and r and l.val == r.val:
                    return dfs(l.left, r.right) and dfs(l.right, r.left)
                else:
                    return False
            
            return dfs(root.left, root.right)   

'''
https://leetcode.com/problems/symmetric-tree/description/
---------------------------------------------------------
Разделяем рут на 2 дерева и пробегаемся по ним, сравнивая зеркальные значения
'''