
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(next=head)

        start, cur = dummy, head 

        for i in range(left - 1):
            start = start.next 
            cur = cur.next 

        prev = None 
        for i in range(right - left + 1):
            nxt = cur.next 
            cur.next = prev 
            prev = cur 
            cur = nxt

        start.next.next = cur
        start.next = prev  
        
        return dummy.next  

'''
https://leetcode.com/problems/reverse-linked-list-ii/description/
-----------------------------------------------------------------
поинтер start, доходим до начала части для реверса (за 1 ноду до), cur ставим на начало части
реверсаем, в cur остался хвост его передаем в start.next.next а реверснутую часть в start.next = prev. 
dummy node для edge кейса где у нас left = 1 
'''