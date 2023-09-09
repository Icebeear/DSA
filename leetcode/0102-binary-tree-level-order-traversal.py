# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(root):
        q = deque()
        res = []
        if root:
            q.append(root)
        
        while q:
            temp = []
            for i in range(len(q)):
                cur = q.popleft()
                temp.append(cur.val)

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)

            res.append(temp)

        return res

'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
----------------------------------------------------------------

'''