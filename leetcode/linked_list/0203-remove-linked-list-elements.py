#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(next=head)
        cur = dummy 

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next 
            else:
                cur = cur.next 

        return dummy.next
    
'''
https://leetcode.com/problems/remove-linked-list-elements/
----------------------------------------------------------

'''