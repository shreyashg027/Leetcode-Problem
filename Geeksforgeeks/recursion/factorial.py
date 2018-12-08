class Solution:
    def fact(self, n):
        if n <= 1:
            return 1
        else:
            return n * self.fact(n-1)


test = Solution()
ans = test.fact(5)
print(ans)

