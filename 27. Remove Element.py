class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return nums


test = Solution()
ans = test.removeElement([], 0)
print(ans)