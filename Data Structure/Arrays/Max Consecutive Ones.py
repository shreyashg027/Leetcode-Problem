class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxCount = -1
        for i in range(len(nums)):
            if nums[i]==1 and i == 0:
                count = 1
            elif nums[i] == 1 and nums[i] == nums[i-1]:
                count += 1
            elif nums[i] == 1 and nums[i] != nums[i-1]:
                if maxCount> count:
                    maxCount = count
                count = 1
        return count


