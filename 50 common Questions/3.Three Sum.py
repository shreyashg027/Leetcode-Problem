class Solution:
    def threeSum(self, nums):
        if len(nums) < 1:
            return []
        sol_set = []
        sortnums = sorted(nums)
        n = len(sortnums)
        for i in range(n-2):
            target = sortnums[i]
            first = i+1
            last = n-1
            while first < last:
                if sortnums[first]+sortnums[last] == -target:
                    triplet = [target, sortnums[first], sortnums[last]]
                    if triplet not in sol_set:
                        sol_set += [triplet]
                    last -= 1
                    first += 1
                elif sortnums[first]+sortnums[last] > -target:
                    last -= 1
                else:
                    first += 1
        return sol_set


test = Solution()
ans = test.threeSum([-2, 0, 1, 1, 2])
print(ans)