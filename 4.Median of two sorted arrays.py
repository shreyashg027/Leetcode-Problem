import math
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1+nums2
        sorted_num = sorted(num)
        n = len(sorted_num)
        if n % 2 == 0:
            median = (sorted_num[round(n/2)-1]+sorted_num[round(n/2)])/2.0
            return median
        else:
            median = sorted_num[int(n/2)]
            return median


test = Solution()
test.findMedianSortedArrays([], [1, 2, 3, 4, 5])
