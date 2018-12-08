class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if nums[i] == 0:
                print(nums[i],nums[i+1])
                nums[i+1],nums[i] = nums[i],nums[i+1]
        print(nums)

test = Solution()
ans = test.moveZeroes([0,1,0,3,12])
# print(ans)

