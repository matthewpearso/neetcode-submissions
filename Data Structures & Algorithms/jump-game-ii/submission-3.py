'''
Intuition:
Use dynamic programming and iterate in reverse using the most optimal way to get to the goal as the subproblem

1) Start at second to last cell

2) On each iteration calculate the lowest number of jumps to reach the goal by using the cells to the right which the value has already been calculated

    dp[i] = 1 + min(all cells in range)

3) the answer should be stored at index 0
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [math.inf] * len(nums)
        dp[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
        
            nextBest = math.inf
            for j in range(i + 1, i + nums[i] + 1):
                if j < len(nums):
                    nextBest = min(nextBest, dp[j])
            
            dp[i] = 1 + nextBest
        
        return dp[0]

        
