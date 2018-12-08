class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            m = nums[i]
            remLis = nums[:i] + nums[i + 1:]
            for item in self.permute(remLis):
                res.append([m]+item)
        return res


test = Solution()
print(test.permute([1, 2, 3]))