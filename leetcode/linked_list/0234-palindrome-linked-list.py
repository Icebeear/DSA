class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        
        # find the middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
 
        # reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    
'''
https://leetcode.com/problems/palindrome-linked-list/
-----------------------------------------------------
находим мидл (slow), потом реверсем и проверяем на палиндром 
'''