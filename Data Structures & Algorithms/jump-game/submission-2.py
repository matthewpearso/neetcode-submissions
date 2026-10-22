class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums) - 1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(nums[i] + 1):
                if i + j < len(dp) and dp[i + j] == True:
                    dp[i] = True
        
        return dp[0]
        
            