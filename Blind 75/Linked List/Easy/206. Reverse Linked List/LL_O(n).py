# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional,ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        temp = None
        prev = None
        
        while (curr):
            temp = curr
            curr = curr.next
            
            temp.next = prev
            prev = temp
        
        return temp
        