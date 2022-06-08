from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Pcurr = 1
        Ncurr = 1
        Tmax = max(nums)
        
        for i in nums:
            temp = Pcurr *i
            Pcurr = max(Pcurr * i, Ncurr * i, i)
            Ncurr = min(temp, Ncurr * i, i) 
            Tmax = max(Pcurr, Tmax)
        return Tmax