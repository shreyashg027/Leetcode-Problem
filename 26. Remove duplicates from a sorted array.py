class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1 and len(nums) > 1:
            if nums[i] == nums[i+1]:
                del nums[i+1]
            else:
                i += 1
        return nums



test = Solution()
ans = test.removeDuplicates([0,1,1,1,2,2,3,4,4,5,5])
print(ans)