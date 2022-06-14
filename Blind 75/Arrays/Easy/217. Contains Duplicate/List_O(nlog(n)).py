from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(set(nums)) == len(nums):
            return False
        return True

    def containsDuplicate2(self, nums: List[int]) -> bool:

        nums = sorted(nums)
        
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                return True
        return False
