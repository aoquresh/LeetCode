# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, TreeNode
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(root:Optional[TreeNode]) -> int:
            if root == None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            
            if left > right:
                return left+1
            return right+1
        
        return depth(root)
            
        