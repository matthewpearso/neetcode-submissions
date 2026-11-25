class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]
            
            isEven = (r - l + 1) % 2 == 0
            if isEven:
                dp[(l, r)] = max(piles[l] + dfs(l + 1, r), piles[r] + dfs(l, r - 1))
            else:
                dp[(l, r)] = max(dfs(l + 1, r), dfs(l, r - 1))
            
            return dp[(l, r)]
        
        return dfs(0, len(piles) - 1) > sum(piles) // 2

