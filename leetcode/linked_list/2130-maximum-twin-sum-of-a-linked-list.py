# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head):
        # fine middle (slow)
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        # reverse second half 
        prev = None 
        while slow:
            nxt = slow.next 
            slow.next = prev 
            prev = slow 
            slow = nxt 

        res = 0
        left, right = head, prev 
        while left and right:
            res = max(res, (left.val + right.val))
            left = left.next 
            right = right.next 
        
        return res

'''
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
----------------------------------------------------------------

'''