class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        indexes = list()
        for i in range(len(nums)):
            if nums[i] == target:
                indexes.append(i)
        return indexes
        
