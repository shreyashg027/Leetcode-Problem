class Solution:
    def sumOfDigits(self,n):
        if n == 0:
            return 0
        return n%10 + self.sumOfDigits(int(n/10))


test = Solution()
ans = test.sumOfDigits(12345)
print(ans)