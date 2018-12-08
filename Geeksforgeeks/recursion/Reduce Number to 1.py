class Solution:
    def reduce(self, n):
        if n == 1:
            # print(n)
            return 0
        if n%2 != 0:
            # print(n)
            return 1+self.reduce(n+1)
        else:
            # print(n)
            return 1+self.reduce(int(n/2))


test = Solution()
print(test.reduce(15))