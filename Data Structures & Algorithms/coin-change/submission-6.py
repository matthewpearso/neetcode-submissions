class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [math.inf] * (amount + 1)
        cache[0] = 0
        
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    cache[i] = min(cache[i], 1 + cache[i - coin])
        
        return cache[amount] if cache[amount] != math.inf else -1

