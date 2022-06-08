from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        bought = prices[0]
        maxProf = 0
        
        for i in prices:
            if i < bought:
                bought = i
            
            elif i - bought > maxProf:
                maxProf = i - bought
        return maxProf
        