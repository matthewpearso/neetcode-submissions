class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(i):
            if i == 0:
                return 0
            
            if i < 0:
                return math.inf
            
            if i in cache:
                return cache[i]
            
            minimum = math.inf
            for coin in coins:
                if amount - coin >= 0:
                    minimum = min(minimum, 1 + dfs(i - coin))
            
            cache[i] = minimum

            return cache[i]
        
        res = dfs(amount)
        
        return res if res != math.inf else -1
        
       
                
                
        