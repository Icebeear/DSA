class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        # find middle (slow)
        slow = head 
        fast = head
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
            
        # merge two halfs
        dummy = ListNode()
        left, right = head, prev
        cur = dummy  
        
        state = True 
        while right and left:
            if state:
                cur.next = left
                left = left.next
                state = False 
            else:
                cur.next = right
                right = right.next 
                state = True 

            cur = cur.next 

        return dummy.next
    
'''
https://leetcode.com/problems/reorder-list/description/
-------------------------------------------------------
находим середины через slow, fast, реверсаем slow и потом мержем head и prev 
'''