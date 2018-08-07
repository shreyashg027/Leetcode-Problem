class Solution:
    def twoSum(self, nums, target):
        dictChar = {}
        if len(nums) < 1:
            return False
        for i in range(len(nums)):
            if nums[i] in dictChar:
                return [dictChar[nums[i]], i]
            else:
                dictChar[target - nums[i]] = i


test = Solution()
ans = test.twoSum([2,7,11,15], 9)
print(ans)
