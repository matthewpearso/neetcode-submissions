class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        
        def dfs(total, i):
            if total == 0:
                return 1

            if total < 0 or i >= len(coins):
                return 0
            
            if (total, i) in dp:
                return dp[(total, i)]
            
            choose = dfs(total - coins[i], i)
            skip = dfs(total, i + 1)
            dp[(total, i)] = choose + skip

            return dp[(total, i)]
        
        return dfs(amount, 0)