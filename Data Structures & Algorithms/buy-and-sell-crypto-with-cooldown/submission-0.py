class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]

        def search(i, status):
            if i >= len(prices):
                return 0
            
            if dp[i][status] != 0:
                return dp[i][status]
            
            if status:
                sell = prices[i] + search(i + 2, 0)
                skip = search(i + 1, 1)
                dp[i][status] = max(sell, skip)
            else:
                buy = -prices[i] + search(i + 1, 1)
                skip = search(i + 1, 0)
                dp[i][status] = max(buy, skip)
            
            return dp[i][status]
        
        return search(0, 0)

