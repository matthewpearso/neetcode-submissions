class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1
        while r < len(prices):
            current_profit = prices[r] - prices[l]
            if current_profit > profit:
                profit = current_profit
            if prices[r] < prices[l]:
                temp = r
                l = temp
                r += 1
            else:
                r += 1
        
        return profit

                
