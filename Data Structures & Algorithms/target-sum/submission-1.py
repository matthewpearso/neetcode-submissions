class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, current):
            
            if i >= len(nums):
                if current == target:
                    return 1
                return 0
            
            # search dp here
            if (i, current) in dp:
                return dp[(i, current)]

            add = dfs(i + 1, current + nums[i])
            sub = dfs(i + 1, current - nums[i])

            dp[(i, current)] = add + sub
            return dp[(i, current)]
        
        return dfs(0, 0)
        