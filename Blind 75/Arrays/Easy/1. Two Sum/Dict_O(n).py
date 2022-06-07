class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = dict()
        
        for ind, val in enumerate(nums):
            if target - val in dic.keys():
                return [ind, dic[target - val]]
            dic[val] = ind
        return