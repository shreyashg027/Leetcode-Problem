class Solution:
    def binaryIncrement(self,n):
        if n == 1:
            return 0
        i = 2
        while i<n:
            i *= 2
        k = n-(i/2)
        temp = self.binaryIncrement(k)
        if temp == 0:
            return 1
        elif temp == 1:
            return 2
        elif temp == 2:
            return 0


test = Solution()
n = 7
print(test.binaryIncrement(n+1))
