# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, val):
        if not root:
            return root

        if val < root.val:
            root.left = self.deleteNode(root.left, val)
        elif val > root.val:
            root.right = self.deleteNode(root.right, val)

        # val found 
        else:
            # Case 1: node to be deleted has no children (leaf node)
            if not root.left and not root.right:
                return None

            # Case 2: node to be deleted has 2 childrens  
            # find the minimum from right subtree 
            elif root.left and root.right:
                cur = root.right 
                while cur.left:
                    cur = cur.left 

                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)

            # Case 3: node has 1 child 
            else:
                child = root.left if root.left else root.right 
                root = child 

        return root 

'''
https://leetcode.com/problems/delete-node-in-a-bst/
---------------------------------------------------
Находим нужную ноду, как нашли если нету детей то возвращаем None, если 2 ребенка то в правой 
ветке находим минималку, заменяем текущий вал на минималку и рекурсивно вызываем тоже самое для для правой ноды 
если 1 ребенок то просто меняем нужную ноду на ребенка  
'''