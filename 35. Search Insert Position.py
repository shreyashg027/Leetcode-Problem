class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = int((start+end)/2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid+1
            else:
                end = mid-1
        return mid+1 if nums[mid]<target else mid

test = Solution()
ans = test.searchInsert([1,3,5,6], 9)
print(ans)

