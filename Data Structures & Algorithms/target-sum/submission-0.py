'''
We will need to start this approach using backtracking and further optimize it using dynamic programming. I'm most comfortable with top-down so I'll be doing that.

We will have a backtracking/dfs function with two params: an Index, i, and a sum starting at 0. 

    Base Cases: 
    1) if we've visited all elements and sum == target, we'll return 1 as one way to get to the target
    2) if sum > target, then it overshoots and returns 0
    3) if we reach the end of the array nums

    Recursive Call:
    We'll have to make a choice between adding or subtracting the current number at index i with our current sum. However, we should probably store each of these decisions in a 2D cache where there are two positions for each decision. So two arrays of len of nums

'''


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def dfs(i, currentSum):

            if i >= len(nums) and currentSum == target:
                return 1
            
            if i >= len(nums):
                return 0
            
            if (i, currentSum) in dp:
                return dp[(i, currentSum)]

            add = dfs(i + 1, currentSum + nums[i])
            subtract = dfs(i + 1, currentSum - nums[i])

            dp[(i, currentSum)] = max(dp.get((i, currentSum), -1), add + subtract)

            return dp[(i, currentSum)]
        
        return dfs(0, 0)
            
            






        