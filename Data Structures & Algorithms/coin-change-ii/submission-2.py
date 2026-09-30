class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        
        def search(i, a):
            if a == amount:
                return 1
            
            if a > amount or i >= len(coins):
                return 0
            
            if (i, a) in dp:
                return dp[(i, a)]
            
            dp[(i, a)] = search(i, a + coins[i]) + search(i + 1, a)
            return dp[(i, a)]
            
        return search(0, 0)
            
            

            


            
