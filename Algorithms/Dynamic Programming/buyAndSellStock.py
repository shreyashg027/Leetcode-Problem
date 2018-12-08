class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        return max_profit

test = Solution()
ans = test.maxProfit([7, 1, 5, 3, 6, 4])
print(ans)