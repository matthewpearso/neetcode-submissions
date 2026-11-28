class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1] * (n + 1)
        def count(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            if num == 2:
                return 1
            
            if dp[num] != -1:
                return dp[num]
            
            dp[num] = count(num - 1) + count(num - 2) + count(num - 3)
            return dp[num]
        
        return count(n)