class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        dictChar = {}
        nums = sorted(nums)
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum == 0:
                    temp = [nums[i],nums[l],nums[r]]
                    if temp not in res:
                        res.append([nums[i],nums[l],nums[r]])
                    l+= 1
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    r-=1
        return res
    def threeSum1(self, nums):
        res = []
        d = {}
        for i,v in enumerate(nums):
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1
        for i,v in enumerate(nums):
            if 
        print(d)


test = Solution()
ans = test.threeSum1([-1,0,1,2,-1,-4])
# print(ans)
