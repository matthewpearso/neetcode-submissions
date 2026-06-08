class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        if len(prices) > 1 :
            opt = prices[r] - prices[l]
        else:
            return 0

        while r <= len(prices) - 1:
            current = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            if current > opt:
                opt = current
            r += 1

        if opt > 0:
            return opt
        else:
            return 0
