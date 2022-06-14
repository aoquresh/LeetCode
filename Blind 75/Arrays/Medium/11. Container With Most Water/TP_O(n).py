from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        currHeight = 0
        
        l, r = 0, len(height)-1
        
        
        while l < r:
            
            width = r - l 
            
            left = height[l]
            right = height[r]
            
            currHeight = min(left, right)
            area = max(area, currHeight*width)
            
            if left > right:
                r -= 1
            else:
                l += 1
                
            
        return area
        