# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head, k):
        cur = head 

        for i in range(k - 1):
            cur = cur.next 
        
        left = cur 
        right = head 

        while cur.next:
            cur = cur.next 
            right = right.next

        left.val, right.val = right.val, left.val 

        return head 

'''
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
--------------------------------------------------------------------------
с помощью 3 указателей, находим cur это левая нода, а потом сохраняем ее в left 
и двигаем cur и right пока cur не упрется и right будет вторым valom.
'''