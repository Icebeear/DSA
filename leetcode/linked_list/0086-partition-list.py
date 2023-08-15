
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        left, right = ListNode(), ListNode()
        cur_left, cur_right = left, right 

        while head:
            if head.val < x:
                cur_left.next = ListNode(head.val)
                cur_left = cur_left.next 
            else:
                cur_right.next = ListNode(head.val)
                cur_right = cur_right.next 

            head = head.next 

        cur_left.next = right.next  
        
        return left.next

'''
https://leetcode.com/problems/partition-list/
---------------------------------------------
2 dummy nodes, если меньше x то в 1, иначе во 2. Потом соединяем
'''