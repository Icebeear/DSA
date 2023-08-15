class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head):
        import math 
        
        cur = head

        while cur.next:
            a = cur.val
            b = cur.next.val 
            val = math.gcd(a, b)
            new_node = ListNode(val=val)

            new_node.next = cur.next 
            cur.next = new_node 
            cur = cur.next.next 
        
        return head
    
'''
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/
-----------------------------------------------------------------------------------------

'''