# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional, ListNode
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None:
            return False
        slow, fast = head, head.next
        
        while fast and fast.next:
            if fast == slow:
                return True
            slow, fast = slow.next, fast.next.next
        return False