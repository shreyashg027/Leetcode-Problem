class Solution:
    def maxSubArray(self, nums):
        low = 0
        high = int(len(nums))-1
        l, r, sum = self.m_sub_array(nums, low, high)
        return sum

    def max_crossing_subarray(self,nums,low,mid, high):
        l_sum = -99999
        sum = 0
        max_left,max_right = 0,0
        for i in range(mid, low-1, -1):
            print('i',i)
            sum += nums[i]
            if sum> l_sum:
                l_sum = sum
                max_left = i
        r_sum = -99999
        sum = 0
        for i in range(mid+1, high+1):
            sum += nums[i]
            if sum> r_sum:
                r_sum = sum
                max_right = i
        return max_left, max_right, l_sum+r_sum

    def m_sub_array(self, nums, low, high):
        if low == high:
            return low, high, nums[low]
        else:
            mid = int((low+high)/2)
            l_low, l_high, l_sum = self.m_sub_array(nums, low, mid)
            r_low, r_high, r_sum = self.m_sub_array(nums, mid+1, high)
            cross_low, cross_high, cross_sum = self.max_crossing_subarray(nums, low, mid, high)
        if l_sum>=r_sum and l_sum>=cross_sum:
            return l_low,l_high,l_sum
        elif r_sum>=l_sum and r_sum>=cross_sum:
            return r_low,r_high,r_sum
        else:
            return cross_low, cross_high,cross_sum


test = Solution()
ans = test.maxSubArray([-1,-1,-2,-2])
print(ans)