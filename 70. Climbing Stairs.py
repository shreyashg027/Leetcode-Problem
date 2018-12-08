class Solution:
    def climbStairs(self, n):
        memo = [0 for i in range(n+1)]
        if n >=4:
            memo[1] = 1
            memo[2] = 2
            memo[3] = 3
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        for i in range(4,n+1):
            memo[i] = memo[i-1]+memo[i-2]
        # print(memo)
        return memo[n]



test = Solution()
ans = test.climbStairs(0)
print(ans)
