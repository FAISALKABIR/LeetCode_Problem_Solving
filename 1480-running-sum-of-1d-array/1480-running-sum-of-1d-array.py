class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        sums = []
        sums.append(nums[0])
        
        for i in range(1, n):
            nums[i] += nums[i-1]
            sums.append(nums[i])
            
        return sums