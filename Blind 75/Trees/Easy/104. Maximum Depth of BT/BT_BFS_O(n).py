# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, TreeNode, deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        if root == None:
            return 0
        
        level = 0
        q = deque([root])
        
        while q:
            
            for i in range(len(q)):
                i = q.popleft()
                if i.left:
                    q.append(i.left)
                if i.right:
                    q.append(i.right)
            
            level += 1
        return level